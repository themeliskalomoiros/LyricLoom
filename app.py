from domna_samiou_scraper import DomnaSamiouScraper


def scrap_domna_samiou_gr():
    url = r'https://www.domnasamiou.gr/?i=portal.el.songs&id=584'
    scraper = DomnaSamiouScraper(url)
    song = scraper.scrap_song()
    print(song)

if __name__ == '__main__':
    scrap_domna_samiou_gr()