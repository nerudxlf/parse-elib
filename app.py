if __name__ == '__main__':
    from src.scraper import Scraper

    with open("data/data.txt", "r", encoding="utf-8") as f:
        text = f.read()
        Scraper(text).start()
