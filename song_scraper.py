
from song_info import SongInfo
from abc import ABC, abstractmethod


class SongScraper(ABC):
    def __init__(self, url):
        self.url = url
        self.soup = page_soup()


    def page_soup(self, url):
        response = requests.get(url)
        if (response.status_code == 200):
            return BeautifulSoup(response.content, 'html.parser')
        else:
            raise PageNotLoadedException(f'Error requesting {url}')


    @abstractmethod
    def get_song_info(self) -> SongInfo:
        pass


    @abstractmethod
    def scrap_title(self):
        pass


    @abstractmethod
    def scrap_lyrics(self):
        pass


    @abstractmethod
    def scrap_release_date(self):
        pass


    @abstractmethod
    def scrap_youtube_url(self):
        pass


    @abstractmethod
    def scrap_spotify_url(self):
        pass


    @abstractmethod
    def scrap_guitar_tabs(self):
        pass


    @abstractmethod
    def scrap_duration(self):
        pass


    @abstractmethod
    def scrap_authors(self):
        pass


    @abstractmethod
    def scrap_composers(self):
        pass


    @abstractmethod
    def scrap_singers(self):
        pass


    @abstractmethod
    def scrap_rhythms(self):
        pass


    @abstractmethod
    def scrap_scales(self):
        pass



class PageNotLoadedException(Exception):
    def __init__(self, message='An error occurred while loading page'):
        self.message = message
        super().__init__(self.message)



class ScrapException(Exception):
    def __init__(self, message='An error occurred while scrapping'):
        self.message = message
        super().__init__(self.message)