from src.scraper import Scraper

if __name__ == '__main__':
    with open("data/data.txt", "r", encoding="utf8") as f:
        text = f.read()
    Scraper(text).start()