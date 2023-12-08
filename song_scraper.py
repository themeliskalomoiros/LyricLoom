
from song_info import SongInfo
from abc import ABC, abstractmethod


class SongScraper(ABC):
    @abstractmethod
    def scrap_song_info(self) -> SongInfo:
        pass



class PageNotLoadedException(Exception):
    """Thrown when a web page could not be loaded."""
    pass



class ScrapException(Exception):
    """Thrown when something went wrong during the scraped of the data."""
    pass