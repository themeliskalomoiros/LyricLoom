# LyricLoom

LyricLoom is a Python application that web scrapes lyrics from a website and populates a database with song information, including lyrics, artists, tags, and more.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/LyricLoom.git
   cd LyricLoom

2. Install dependencies:
    ```bash
    pip install -r requirements.txt


## Usage

Run the LyricLoom application to scrape lyrics and populate the database (there will be a Sqlite file named 'lyrics.db' created for you the first time). Currently it scraps old greek traditional songs from [domna samiou's](https://www.domnasamiou.gr/) website, but it can be extended to scrap data from every website.


## Features

- Web scrapes lyrics from a specified website.
- Populates a SQLite database with song information.
- Supports multiple artists, tags, and other metadata.

## Contributing

Contributions are welcome! If you'd like to contribute to LyricLoom, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.


### Add another website
In case you want to crawl another website extend `SongScraper` and implement the abstract methods.
Then swap your own scraper with `DomnaSamiouScraper` in the `app.py`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
