from typing import Any

from pydantic import StrictInt, field_validator  # pylint: disable = E0401 # type: ignore
from pydantic.dataclasses import dataclass  # pylint: disable = E0401 # type: ignore

from src.domain.entities.status import Status


@dataclass(slots=True, kw_only=True, validate_on_init=True)
class Book:
    title: str
    author: str
    volume: StrictInt = 0
    status: Status = Status.NOT_STARTED

    @field_validator("title", "author", mode="before")
    def not_empty(cls, value: str, field: Any) -> str:
        if len(value) < 3:
            raise ValueError(f"O campo '{field.field_name}' deve ter pelo menos 3 caracteres")
        return value

    @field_validator("volume")
    def check_volume(cls, value: StrictInt) -> StrictInt:
        if value < 0:
            raise ValueError("O volume nao deve ser negativo")
        return value

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_volume(self) -> StrictInt:
        return self.volume

    def get_status(self) -> Status:
        return self.status
