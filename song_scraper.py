import requests
from bs4 import BeautifulSoup
from song_info import SongInfo
from abc import ABC, abstractmethod


class SongScraper(ABC):
    def __init__(self, url):
        self.url = url
        self.soup = self.init_soup()


    def init_soup(self):
        response = requests.get(self.url)
        if (response.status_code == 200):
            return BeautifulSoup(response.content, 'html.parser')
        else:
            raise PageNotLoadedException(f'Error requesting {self.url}')


    @abstractmethod
    def get_song_info(self) -> SongInfo:
        pass


    @abstractmethod
    def scrap_title(self) -> str:
        pass


    @abstractmethod
    def scrap_lyrics(self) -> str:
        pass


    @abstractmethod
    def scrap_release_date(self) -> str:
        pass


    @abstractmethod
    def scrap_youtube_url(self) -> str:
        pass


    @abstractmethod
    def scrap_spotify_url(self) -> str:
        pass


    @abstractmethod
    def scrap_guitar_tabs(self) -> str:
        pass


    @abstractmethod
    def scrap_duration(self) -> str:
        pass


    @abstractmethod
    def scrap_authors(self) -> list:
        pass


    @abstractmethod
    def scrap_composers(self) -> list:
        pass


    @abstractmethod
    def scrap_singers(self) -> list:
        pass


    @abstractmethod
    def scrap_rhythms(self) -> list:
        pass


    @abstractmethod
    def scrap_scales(self) -> list:
        pass


    @abstractmethod
    def scrap_tags(self) -> list:
        pass



class PageNotLoadedException(Exception):
    def __init__(self, message='An error occurred while loading page'):
        self.message = message
        super().__init__(self.message)



class ScrapException(Exception):
    def __init__(self, message='An error occurred while scrapping'):
        self.message = message
        super().__init__(self.message)