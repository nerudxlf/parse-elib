import json


class Article:
    def __init__(self, title, authors, source, year, value, citations):
        self.title = title
        self.author = authors
        self.source = source
        self.year = year
        self.value = value
        self.citations = citations
        
    def to_json(self):
        return json.dumps({
            "Название": self.title,
            "Авторы": self.author,
            "Журнал": self.source,
            "Год публикации": self.year,
            "Том": self.value,
            "Цитирования": self.citations,
        }, ensure_ascii=False, separators=(',', ': '))

    def __str__(self):
        return f"Название {self.title} Авторы {self.author} Журнал {self.source} Год {self.year} Том {self.value} Цитирования {self.citations}"

    def __repr__(self):
        return f"Название {self.title} Авторы {self.author} Журнал {self.source} Год {self.year} Том {self.value} Цитирования {self.citations}"
