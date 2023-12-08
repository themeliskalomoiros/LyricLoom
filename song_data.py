from models import Song, Artist


class SongData:
    def __init__(self):
        self.song = None
        self.authors = set()
        self.singers = set()
        self.composers = set()


    def add_author(self, author):
        self.authors.append(author)


    def add_singer(self, singer):
        self.singers.append(singer)


    def add_composer(self, composer):
        self.composers.append(composer)