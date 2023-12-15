import os
import sqlite3
from sql_repo import SqlRepo
from progress_bar import printProgressBar
from domna_samiou_scraper import DomnaSamiouScraper
from song_scraper import PageNotLoadedException, ScrapException
from song_repo import SongAlreadyExistException, InvalidArtistException, InvalidTagException


db_file = 'lyrics.db'

def create_db_if_not_exist():
    schema_file = 'schema.sql'

    if not os.path.exists(db_file):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()

            with open(schema_file, 'r') as schema_file:
                schema_script = schema_file.read()
                cursor.executescript(schema_script)

            conn.commit()

        print(f'Created database file {db_file}.')


def log(successful_insertions, failed_insertions):
    f = open('log.txt', 'w')
    f.write(f'Inserted:\t\t{successful_insertions}')
    f.write(f'\nFailed:\t\t\t{failed_insertions}')
    f.write(f'\nTotal:\t\t\t{failed_insertions + successful_insertions}')
    f.close()


def urls(song_web_ids):
    default_url = r'https://www.domnasamiou.gr/?i=portal.el.songs&id='
    urls = []
    for _id in song_web_ids:
        urls.append(f'{default_url}{_id}')
    return urls


def domna_samiou_gr():
    create_db_if_not_exist()
    progress = 1
    progressMax = 930
    insertions = 0
    failed_insertions = 0
    repo = SqlRepo(db_file)


    for url in urls(range(progress, progressMax)):
        printProgressBar(
            progress,
            progressMax,
            prefix = 'Progress:',
            suffix = 'Complete',
            length = 100)

        progress += 1

        try:
            scraper = DomnaSamiouScraper(url)
            scraper.scrap_title()
            scraper.scrap_lyrics()
            scraper.scrap_youtube_url()
            scraper.scrap_spotify_url()
            scraper.scrap_authors()
            scraper.scrap_composers()
            scraper.scrap_singers()
            scraper.scrap_spotify()
            scraper.scrap_tags()

            repo.save(scraper.get_song_info())
            insertions += 1
            if insertions % 100 == 0:
                repo.commit()

        except (ScrapException, PageNotLoadedException, SongAlreadyExistException, InvalidArtistException, InvalidTagException):
            failed_insertions += 1
            log(insertions, failed_insertions)


    printProgressBar(
        1,
        1,
        prefix = 'Progress:',
        suffix = 'Complete',
        length = 100)

    repo.commit()
    repo.close()


if __name__ == '__main__':
    domna_samiou_gr()
