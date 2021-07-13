from dataclasses import dataclass
import uuid
import book_query


@dataclass
class Book():
    title: str
    description: str
    content: str
    image_url: str

    def create_book(self) -> str:
        book_query.create_book(self)
        return "Book Created"

    def update_book(self, id) -> str:
        return "Book Updated"

    def delete_book(self, id) -> str:
        return "Book Deleted"

    def fetch_books(self, id) -> str:
        return "Books Fetched Successfully"

    def search_book(self, search_key) -> str:
        return "Book Found"

    def add_favorite(self, id) -> str:
        return "Added to Favorite"