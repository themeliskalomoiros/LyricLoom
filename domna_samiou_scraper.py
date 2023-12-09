import requests
from models import Artist, paradosiako_artist, unknown_artist
from bs4 import BeautifulSoup
from song_repo import SongRepo
from song_info import SongInfo
from song_scraper import SongScraper, PageNotLoadedException, ScrapException


class DomnaSamiouScraper(SongScraper):
    PARADOSI = paradosiako_artist()


    def __init__(self, song_url):
        self.url = song_url
        self.soup = self.page_soup(self.url)


    def scrap_song_info(self):
        title = self.scrap_title()
        lyrics = self.scrap_lyrics()
        youtube = self.scrap_youtube()
        spotify = self.scrap_spotify()
        info = SongInfo(title, lyrics, None, youtube, spotify)
        
        info.add_author(self.PARADOSI)
        info.add_composer(self.PARADOSI)
        
        singers = self.scrap_singers()
        for s in singers:
            info.add_singer(s)

        tags = self.scrap_tags()
        for t in tags:
            info.add_tag(t)

        return info


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
        ul_tags = self.soup.find(id='song-info').find_all('ul')
        
        for ul in ul_tags:
            for li in ul.children:
                prefix = 'Τραγούδι:'
                li_text = li.get_text()

                if prefix in li_text:
                    # Singers found
                    li_text = li_text.removeprefix(prefix).strip()
                    if ',' in li_text:
                        # Many singers
                        singer_strings =  li_text.split(',')
                        for i in range(0, len(singer_strings)):
                            singer_strings[i] = singer_strings[i].strip()
                        singers = []
                        for s in singer_strings:
                            first_last = s.split()
                            singers.append(Artist(first_last[0], first_last[1]))
                        return singers
                    else:
                        # One singer
                        first_last = li_text.split()
                        if len(first_last) > 0:
                            if len(first_last) > 1:
                                return [Artist(first_last[0], first_last[1])]
                            else:
                                return [Artist(first_last[0], '')]
        return [unknown_artist()]


    def scrap_tags(self):
        tags = []
        div = self.soup.find(id='song-info')
        
        if div:
            ul = div.find('ul')
            if ul:
                li_texts = [li.get_text(strip=True) for li in ul.find_all('li')]
                tag_labels = ['Προέλευση:', 'Ταξινόμηση:', 'Τόπος:']
                for text in li_texts:
                    for label in tag_labels:
                        if label in text:
                            text = text.removeprefix(label)
                            if ',' in text:
                                # Ex, 'Ταξινόμιση' could include 'Της Αγαπης, Του έρωτά' (2 values)
                                many_tags_in_label = text.split(',')
                                for tag in many_tags_in_label:
                                    tags.append(tag.strip())
                            else:
                                tags.append(text.removeprefix(label).strip())

        return tags


    def page_soup(self, url):
        response = requests.get(url)
        if (response.status_code == 200):
            return BeautifulSoup(response.content, 'html.parser')
        else:
            raise PageNotLoadedException(f'Error requesting {url}')

