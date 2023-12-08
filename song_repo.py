from song_info import SongInfo
from abc import ABC, abstractmethod


class SongRepo(ABC):
    @abstractmethod
    def save(self, song_info):
        pass