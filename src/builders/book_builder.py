from pydantic import StrictInt  # pylint: disable = E0401 # type: ignore
from pydantic.dataclasses import dataclass  # pylint: disable = E0401 # type: ignore
from typing_extensions import Self  # pylint: disable = E0401 # type: ignore

from src.domain import Book, Status


@dataclass(slots=True, kw_only=True, validate_on_init=True)
class BookBuilder:
    title: str = "1984"
    author: str = "George Orwell"
    volume: StrictInt = 0
    status: Status = Status.NOT_STARTED

    def with_title(self, title: str) -> Self:
        self.title = title
        return self

    def with_author(self, author: str) -> Self:
        self.author = author
        return self

    def with_volume(self, volume: StrictInt) -> Self:
        self.volume = volume
        return self

    def with_status(self, status: Status) -> Self:
        self.status = status
        return self

    def build(self) -> Book:
        return Book(title=self.title, author=self.author, volume=self.volume, status=self.status)
