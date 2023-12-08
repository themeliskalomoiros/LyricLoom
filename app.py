from sql_repo import SqlRepo
from domna_samiou_scraper import DomnaSamiouScraper
from song_scraper import PageNotLoadedException, ScrapException
from song_repo import SongAlreadyExistException, InvalidArtistException, InvalidTagException


def urls(song_web_ids):
    default_url = r'https://www.domnasamiou.gr/?i=portal.el.songs&id='
    urls = []
    for _id in song_web_ids:
        urls.append(f'{default_url}{_id}')
    return urls


def domna_samiou_gr():
    repo = SqlRepo('stixoi.db')
    for url in urls(range(1, 5)):
        try:
            scraper = DomnaSamiouScraper(url)
            song = scraper.scrap_song_info()
            repo.save(song)
        except ScrapException:
            # TODO: scraper.url should be a property of the parent class
            print(f'Scrap-Error: during scrap of {scraper.url}')
        except PageNotLoadedException:
            print(f'Scrap-Error: could not load page {scraper.url} (internet connection OK?)')
        except SongAlreadyExistException:
            print(f'Repo-Error: song {song.song.Title} already exists.')
        except InvalidArtistException:
            print(f'Repo-Error: invalid artist for song {song.song.Title}')
        except InvalidTagException:
            print(f'Repo-Error: invalid tag for song {song.song.Title}')


if __name__ == '__main__':
    domna_samiou_gr()