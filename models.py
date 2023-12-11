class Song:
    def __init__(self):
        self.title = None
        self.lyrics = None
        self.year = None
        self.youtube = None
        self.spotify = None
        self.guitar_tabs = None
        self.duration = None


    def __str__(self):
        s = f'Title: <{self.title}>'
        s += f'\nYear: <{self.title}>'
        s += f'\nYoutube: <{self.title}>'
        s += f'\nSpotify: <{self.title}>'
        s += f'\nDuration: <{self.title}>'
        s += f'\nLyrics: <{self.title}>'
        s += f'\nGuitar Tabs: <{self.title}>'
        return s


    def __eq__(self, other):
        if isinstance(other, Song):
            return self.title == other.title and self.lyrics == other.lyrics
        return False


    def __hash__(self):
        return hash((self.title, self.lyrics))


class Artist:
    def __init__(self):
        self.firstname = None
        self.lastname = None


    def __str__(self):
        return f'Artist: {self.firstname} {self.lastname}'


    def paradosi():
        return Artist('Παραδοσιακό', '')


    def unknown():
        return Artist('Άγνωστος', 'Καλλιτέχνης')


    def __eq__(self, other):
        if isinstance(other, Artist):
            return self.firstname == other.firstname and self.lastname == other.lastname
        return False


    def __hash__(self):
        return hash((self.firstname, self.lastname))


