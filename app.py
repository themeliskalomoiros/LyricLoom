from sql_repo import SqlRepo
from progress_bar import printProgressBar
from domna_samiou_scraper import DomnaSamiouScraper
from song_scraper import PageNotLoadedException, ScrapException
from song_repo import SongAlreadyExistException, InvalidArtistException, InvalidTagException


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
    
    progress = 1
    progressMax = 4 
    insertions = 0
    failed_insertions = 0
    repo = SqlRepo('stixoi.db')


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
            info = scraper.scrap_song_info()
            repo.save(info)
            insertions += 1
        except ScrapException:
            failed_insertions += 1
            log(insertions, failed_insertions)
        except PageNotLoadedException:
            failed_insertions += 1
            log(insertions, failed_insertions)
        except SongAlreadyExistException:
            failed_insertions += 1
            log(insertions, failed_insertions)
        except InvalidArtistException:
            failed_insertions += 1
            log(insertions, failed_insertions)
        except InvalidTagException:
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