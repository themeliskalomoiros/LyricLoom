import requests
from models import Artist, paradosiako_artist
from bs4 import BeautifulSoup
from song_repo import SongRepo
from song_info import SongInfo
from song_scraper import SongScraper, PageNotLoadedException, ScrapException


class DomnaSamiouScraper(SongScraper):
    PARADOSI = paradosiako_artist()


    def __init__(self, song_url):
        self.url = song_url
        self.soup = self.page_soup(self.url)


    def scrap_song(self):
        title = self.scrap_title()
        lyrics = self.scrap_lyrics()
        youtube = self.scrap_youtube()
        spotify = self.scrap_spotify()
        song = SongInfo(title, lyrics, None, youtube, spotify)
        
        song.add_author(self.PARADOSI)
        song.add_composer(self.PARADOSI)
        
        singers = self.scrap_singers()
        for s in singers:
            song.add_singer(s)

        return song


    def scrap_title(self):
        title_tag = self.soup.find(id='item-title')

        if title_tag:
            return title_tag.get_text(strip=True)
        else:
            raise ScrapException(f'Title not scraped {self.url}')


    def scrap_lyrics(self):
        lyrics_tag = self.soup.find(id='item-lyrics')

        if lyrics_tag:
            return lyrics_tag.get_text(strip=True)
        else:
            raise ScrapException(f'Lyrics not scraped {self.url}')


    def scrap_youtube(self):
        youtube_tag = self.soup.find(id='tools-youtube-music')

        if youtube_tag:
            return youtube_tag.get('href')


    def scrap_spotify(self):
        spotify_tag = self.soup.find('a', id='tools-spotify')

        if spotify_tag:
            return spotify_tag.get('href')
            

    def scrap_singers(self):
        tag = self.soup.find(id='song-info')

        if tag:
            # The text retrieved has this structure...
            # ΤΡΑΓΟΥΔΙ: Δόμνα Σαμίου, Θεοπούλα Δοϊτσίδη, Μόρφω Δοϊτσίδη
            text = tag.get_text(strip=True)
            text = text.split('Δισκογραφία')[0]
            index_of_tragoudi = text.find('Τραγούδι:')
            text = text[index_of_tragoudi + len('Τραγούδι:'):]
            singer_names = text.split(',')
            for i in range(0, len(singer_names)):
                singer_names[i] = singer_names[i].strip()
            singers = []
            for item in singer_names:
                first_and_lastname = item.split()
                singers.append(Artist(first_and_lastname[0], first_and_lastname[1]))
            return singers
        else:
            raise ScrapException(f'Singers not scraped {self.url}')



    def page_soup(self, url):
        response = requests.get(url)
        if (response.status_code == 200):
            return BeautifulSoup(response.content, 'html.parser')
        else:
            raise PageNotLoadedException(f'Error requesting {url}')

