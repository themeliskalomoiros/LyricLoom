from song_data import SongData
from abc import ABC, abstractmethod


class SongRepo(ABC):
    @abstractmethod
    def save(self, song):
        pass