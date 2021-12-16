from bs4 import BeautifulSoup, Tag

from src.dbo import Article


class Scraper:
    _soup: BeautifulSoup = None

    def __init__(self, text):
        self.html_text = text
        self._soup = BeautifulSoup(self.html_text, "lxml")

    def get_list_elements(self) -> list[Tag]:
        return self._soup.find("table", {"id": "restab"}).find_all("tr")[3:]

    @staticmethod
    def _get_title(td: Tag) -> str:
        data = td.find("b").text
        return data

    @staticmethod
    def _get_authors(td: Tag) -> str:
        data = td.find("i").text
        return data

    @staticmethod
    def _get_source(td: Tag) -> str:
        data = td.find_all("font")[1].find_all("a")[0].text
        return data

    @staticmethod
    def _get_year(td: Tag) -> str:
        data = td.find_all("font")[1].text
        data_split = data.split("\n")[2]
        return data_split

    @staticmethod
    def _get_citations(td: Tag) -> str:
        return td.text.replace("\n", "")

    @staticmethod
    def _get_value(td: Tag) -> str:
        data = td.find_all("font")[1].text
        data_split = data.split("\n")[3].replace("\\xa0", "")
        return data_split

    def _parse_td_elements(self, tr: Tag):
        get_center_td, get_right_td, *_ = tr.find_all("td")[1:]
        title = self._get_title(get_center_td)
        authors = self._get_authors(get_center_td)
        source = self._get_source(get_center_td)
        year = self._get_year(get_center_td)
        value = self._get_value(get_center_td)
        citations = self._get_citations(get_right_td)
        return Article(title, authors, source, year, value, citations)

    def start(self):
        list_elements = self.get_list_elements()
        result_data = []
        for i in list_elements:
            result_data.append(self.parse_td_elements(i))
        return result_data
