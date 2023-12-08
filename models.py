class Song:
    def __init__(
        self, 
        title, 
        lyrics, 
        year = None, 
        youtube = None):
        self.title = title
        self.lyrics = lyrics
        self.year = year
        self.youtube = youtube


    def __str__(self):
        s = f'Song: {self.title}'
        
        if self.year:
            s += f' ({self.year})'
        if self.youtube:
            s += f'\nYoutube: {self.year}'
        
        s += f'\nLyrics:\n{self.lyrics}'

        return s


    def __eq__(self, other):
        if isinstance(other, Song):
            return self.title == other.title and self.lyrics == other.lyrics
        return False


    def __hash__(self):
        return hash((self.title, self.lyrics))


class Artist:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


    def __str__(self):
        return f'Artist: {self.firstname} {self.lastname}'


    def __eq__(self, other):
        if isinstance(other, Artist):
            return self.firstname == other.firstname and self.lastname == other.lastname
        return False


    def __hash__(self):
        return hash((self.firstname, self.lastname))



def unknown_artist():
    return Artist('Άγνωστος', 'Καλλιτέχνης')