class Song:
    def __init__(
        self,
        title=None,
        lyrics=None,
        year=None,
        youtube=None,
        spotify=None,
        guitar_tabs=None,
        duration=None):
        self.title = title
        self.lyrics = lyrics
        self.year = year
        self.youtube = youtube
        self.spotify = spotify
        self.guitar_tabs = guitar_tabs
        self.duration = duration


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
    def __init__(
        self, 
        firstname=None, 
        lastname=None):
        self.firstname = None
        self.lastname = None


    def __str__(self):
        return f'Firstname: <{self.firstname}>\nLastname: <{self.lastname}>'


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



class Rhythm:
    def __init__(
        self, 
        name=None,
        tempo=None):
        self.name = name
        self.tempo = tempo


    def __str__(self):
        return f'Name: <{self.name}>\nTempo: <{self.tempo}>'


    def __eq__(self, other):
        if isinstance(other, Rhythm):
            return self.name == other.name and self.tempo == other.tempo
        return False


    def __hash__(self):
        return hash((self.name, self.tempo))


class Scale:
    def __init__(
        self,
        name=None,
        is_minor=None,
        original_tone=None):
        self.name = name        
        self.is_minor = is_minor
        self.original_tone = original_tone


    def __str__(self):
        s = f'Name: <{self.name}>'
        s += f'\nIs Minor: <{self.is_minor}>'
        s += f'\nOriginal Tone: <{self.original_tone}>'
        return s


    def __eq__(self, other):
        if isinstance(other, Rhythm):
            return self.name == other.name and self.is_minor == other.is_minor and self.original_tone == other.original_tone
        return False


    def __hash__(self):
        return hash((self.name, self.is_minor, self.original_tone))