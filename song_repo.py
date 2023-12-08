from song_info import SongInfo
from abc import ABC, abstractmethod


class SongRepo(ABC):
    @abstractmethod
    def save(self, song_info):
        pass
        


class SongAlreadyExistException(Exception):
    pass



class InvalidArtistException(Exception):
    pass



class InvalidTagException(Exception):
    pass