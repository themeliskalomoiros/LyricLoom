import models
import sqlite3
from song_repo import *
from song_info import SongInfo


INVALID_ROW_ID = -1


class SqlRepo(SongRepo):
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def save(self, song_info):
        song_id = self.insert_song(song_info.song)

        artist_ids = self.insert_artists(song_info.authors)
        self.connect_authors(song_id, artist_ids)

        artist_ids = self.insert_artists(song_info.composers)
        self.connect_composers(song_id, artist_ids)

        artist_ids = self.insert_artists(song_info.singers)
        self.connect_singers(song_id, artist_ids)
        
        tag_ids = self.insert_tags(song_info.tags)
        self.connect_tags(song_id, tag_ids)


    def insert_song(self, song):
        query = 'INSERT INTO Songs(Title, Lyrics, ReleaseDate, YoutubeLink) VALUES(?, ?, ?, ?)'
        values = (song.title, song.lyrics, song.year, song.youtube)
        try:
            self.cursor.execute(query, values)
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise SongAlreadyExistException(f"Song {song} exists.")


    def insert_artists(self, artists): 
        ids = set()
        for a in artists:
            ids.add(self.insert_artist(a))
        return ids


    def insert_artist(self, artist):
        query = 'INSERT INTO Artists(Firstname, Lastname) VALUES(?, ?)'
        values = (artist.firstname, artist.lastname)
        try:
            self.cursor.execute(query, values)
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            _id = self.artist_database_id(artist)
            if _id == INVALID_ROW_ID:
                raise InvalidArtistException(f'Something went wrong with artist {artist}')
            else:
                return _id


    def artist_database_id(self, artist):
        query = 'SELECT ArtistID FROM Artists WHERE Firstname = ? AND Lastname = ?'
        values = (artist.firstname, artist.lastname)
        self.cursor.execute(query, values)
        id_tuple = self.cursor.fetchone()

        if id_tuple and len(id_tuple) > 0:
            return id_tuple[0]
        else:
            return INVALID_ROW_ID


    def connect_authors(self, song_id, author_ids):
        for _id in author_ids:
            query = 'INSERT INTO SongsAuthors(SongID, AuthorID) VALUES(?, ?)'
            values = (song_id, _id)
            self.cursor.execute(query, values)


    def connect_composers(self, song_id, composer_ids):
        for _id in composer_ids:
            query = 'INSERT INTO SongsComposers(SongID, ComposerID) VALUES(?, ?)'
            values = (song_id, _id)
            self.cursor.execute(query, values)


    def connect_singers(self, song_id, singer_ids):
        for _id in singer_ids:
            query = 'INSERT INTO SongsSingers(SongID, SingerID) VALUES(?, ?)'
            values = (song_id, _id)
            self.cursor.execute(query, values)


    def insert_tags(self, tags):
        ids = set()
        for t in tags:
            ids.add(self.insert_tag(t))
        return ids


    def insert_tag(self, tag):
        query = 'INSERT INTO Tags(Label) VALUES(?)'
        values = (tag)
        try:
            self.cursor.execute(query, values)
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            _id = self.tag_database_id(tag)
            if _id == INVALID_ROW_ID:
                raise InvalidTagException(f'Something went wrong with tag {tag}')
            else:
                return _id


    def tag_database_id(self, tag):
        query = 'SELECT TagID FROM Tags WHERE Label = ?'
        values = (tag)
        self.cursor.execute(query, values)
        id_tuple = self.cursor.fetchone()

        if id_tuple and len(id_tuple) > 0:
            return id_tuple[0]
        else:
            return INVALID_ROW_ID


    def connect_tags(self, song_id, tag_ids):
        for _id in tag_ids:
            query = 'INSERT INTO SongsTags(SongID, TagID) VALUES(?, ?)'
            values = (song_id, _id)
            self.cursor.execute(query, values)


    def close(self):
        self.connection.close()


    def commit(self):
        self.connection.commit()

