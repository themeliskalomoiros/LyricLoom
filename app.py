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
    for url in urls(range(1, 4)):
        try:
            scraper = DomnaSamiouScraper(url)
            info = scraper.scrap_song_info()
            repo.save(info)
        except ScrapException:
            # TODO: scraper.url should be a property of the parent class
            print(f'Scraper: error during scrap of {scraper.url}')
        except PageNotLoadedException:
            print(f'Scraper: could not load page {scraper.url} (internet connection OK?)')
        except SongAlreadyExistException:
            print(f'Repo: song {info.song.title} already exists.')
        except InvalidArtistException:
            print(f'Repo: invalid artist for song {info.song.title}')
        except InvalidTagException:
            print(f'Repo: invalid tag for song {info.song.title}')
    repo.commit()
    repo.close()


if __name__ == '__main__':
    domna_samiou_gr()