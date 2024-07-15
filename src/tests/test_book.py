import pytest  # type: ignore
from pydantic import ValidationError  # type: ignore

from src.builders import BookBuilder
from src.domain import Book, Status


@pytest.fixture
def book_builder():
    return (
        BookBuilder()
        .with_title("Fahrenheit 451")
        .with_author("Ray Bradbury")
        .with_volume(1)
        .with_status(Status.STARTED)
        .build()
    )


def test_instanciar_livro(book_builder: Book):
    assert isinstance(book_builder, Book)


def test_book_creation(book_builder: Book):
    assert book_builder.title == book_builder.get_title()
    assert book_builder.author == book_builder.get_author()
    assert book_builder.volume == book_builder.get_volume()
    assert book_builder.status == book_builder.get_status()


def test_default_user_creation():
    book_builder = BookBuilder().build()
    assert book_builder.title == book_builder.get_title()
    assert book_builder.author == book_builder.get_author()
    assert book_builder.volume == book_builder.get_volume()
    assert book_builder.status == book_builder.get_status()


@pytest.mark.parametrize(
    "tittle, author, volume, expected_error_message",
    [
        ("", "George Orwell", 1, "O campo 'title' deve ter pelo menos 3 caracteres"),
        ("1984", "", 1, "O campo 'author' deve ter pelo menos 3 caracteres"),
        ("1984", "George Orwell", -1, "O volume nao deve ser negativo"),
    ],
)
def test_register_book_missing_parameters(tittle: str, author: str, volume: int, expected_error_message: str):
    with pytest.raises(ValidationError, match=expected_error_message):
        BookBuilder().with_title(tittle).with_author(author).with_volume(volume).build()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
