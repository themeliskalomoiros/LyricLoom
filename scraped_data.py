from models import Song, Artist


class ScrapedData:
    def __init__(self):
        self.song = None
        self.authors = []
        self.singers = []
        self.composers = []