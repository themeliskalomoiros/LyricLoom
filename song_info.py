from models import Song, Artist


class SongInfo:
    def __init__(
        self,
        title = None, 
        lyrics = None, 
        year = None, 
        youtube = None, 
        spotify = None):
        self.song = Song(title, lyrics, year, youtube, spotify)
        self.tags = set()
        self.authors = set()
        self.singers = set()
        self.composers = set()


    def add_tag(self, tag):
        self.tags.add(tag)


    def add_author(self, author):
        self.authors.add(author)


    def add_singer(self, singer):
        self.singers.add(singer)


    def add_composer(self, composer):
        self.composers.add(composer)


    def __str__(self):
        s = f'Title: {self.song.title}\nYear: {self.song.year}'
        s += f'\nYoutube: {self.song.youtube}'
        s += f'\nSpotify: {self.song.spotify}'
        s += f'\nLyrics: \n{self.song.lyrics}'

        s += '\n\nAuthors:'
        for a in self.authors:
            s += f'\n{a}'
        s += '\n\nComposers:'
        for a in self.composers:
            s += f'\n{a}'
        s += '\n\nSingers:'
        for a in self.singers:
            s += f'\n{a}'

        s += '\n\nTags:'
        for t in self.tags:
            s += f'\n{t}'

        return s