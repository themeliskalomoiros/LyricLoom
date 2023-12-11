from song_scraper import *
from models import Artist
from song_info import SongInfo


class DomnaSamiouScraper(SongScraper):
    GREEK_TRADITION = Artist('Παραδοσιακό', '')
    UNKNOWN_ARTIST = Artist('Άγνωστος', 'Καλλιτέχνης')


    def __init__(self, url):
        super().__init__(url)
        self.song_info = SongInfo()


    def get_song_info(self) -> SongInfo:
        return self.song_info


    def scrap_title(self):
        tag = self.soup.find(id='item-title')

        if tag:
            title = tag.get_text(strip=True)
            if title:
                self.song_info.set_title(title)
            else:
                raise ScrapException(f'Title is null {self.url}')
        else:
            raise ScrapException(f'Title not scraped {self.url}')


    def scrap_lyrics(self):
        tag = self.soup.find(id='item-lyrics')

        if tag:
            lyrics = tag.get_text(strip=True)
            if lyrics:
                self.song_info.set_lyrics(lyrics)
            else:
                raise ScrapException(f'Lyrics are null: {self.url}')
        else:
            raise ScrapException(f'Lyrics not scraped: {self.url}')


    def scrap_release_date(self):
        pass


    def scrap_youtube_url(self):
        tag = self.soup.find(id='tools-youtube-music')
        if tag:
            url = tag.get('href')
            if url:
                self.song_info.set_youtube(url)


    def scrap_spotify_url(self):
        tag = self.soup.find('a', id='tools-spotify')
        if tag:
            url = tag.get('href')
            if url:
                self.song_info.set_spotify(url)


    def scrap_guitar_tabs(self):
        # Not available in the website.
        pass


    def scrap_duration(self):
        # Not available in the website.
        pass


    def scrap_authors(self):
        self.song_info.add_author(self.GREEK_TRADITION)


    def scrap_composers(self):
        self.song_info.add_composer(self.GREEK_TRADITION)


    def scrap_singers(self):
        singers = self.extract_singers()
        self.song_info.singers.update(singers)


    def scrap_rhythms(self):
        # Not available in the website.
        pass


    def scrap_scales(self):
        # Not available in the website.
        pass


    def scrap_spotify(self):
        spotify_tag = self.soup.find('a', id='tools-spotify')

        if spotify_tag:
            return spotify_tag.get('href')


    def scrap_tags(self):
        tags = self.extract_tags()
        self.song_info.tags.update(tags)
            

    def extract_singers(self):
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
        return [self.UNKNOWN_ARTIST]


    def extract_tags(self):
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

