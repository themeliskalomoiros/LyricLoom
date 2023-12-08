from song_data import SongData
from abc import ABC, abstractmethod


class SongScraper(ABC):
    def __init__(self, song_url):
        self.song_url = song_url


    @abstractmethod
    def scrap_song(self):
        pass