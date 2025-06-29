class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self._pages = value

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value) -> None:
        if not isinstance(value, float):
            raise TypeError
        if value <= 0:
            raise ValueError
        self._duration = value

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность: {self.duration:.2f} ч"
