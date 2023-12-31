from models import Song, Artist


class SongInfo:
    def __init__(self):
        self.song = Song()
        self.tags = set()
        self.scales = set()
        self.rhythms = set()
        self.authors = set()
        self.singers = set()
        self.composers = set()


    def set_title(self, title):
        self.song.title = title


    def set_lyrics(self, lyrics):
        self.song.lyrics = lyrics


    def set_year(self, year):
        self.song.year = year


    def set_youtube(self, youtube):
        self.song.youtube = youtube


    def set_spotify(self, spotify):
        self.song.spotify = spotify


    def set_guitar_tabs(self, guitar_tabs):
        self.song.guitar_tabs = guitar_tabs


    def set_duration(self, duration):
        self.song.duration = duration

        
    def add_tag(self, tag):
        self.tags.add(tag)


    def add_rhythm(self, rhythm):
        self.rhythms.add(rhythm)


    def add_scale(self, scale):
        self.scales.add(scale)


    def add_author(self, author):
        self.authors.add(author)


    def add_singer(self, singer):
        self.singers.add(singer)


    def add_composer(self, composer):
        self.composers.add(composer)


    def __str__(self):
        s = f'\tSong\n{self.song}'      
        s += '\n\tTags'
        for t in self.tags:
            s += f'\n{t}'
        s += '\n\tAuthors'
        for a in self.authors:
            s += f'\n{a}'
        s += '\n\tComposers'
        for a in self.composers:
            s += f'\n{a}'
        s += '\n\tSingers'
        for a in self.singers:
            s += f'\n{a}'
        s += '\n\tRhythms'
        for r in self.rhythms:
            s += f'\n{r}'
        s += '\n\tScales'
        for a in self.scales:
            s += f'\n{a}'
        return s
