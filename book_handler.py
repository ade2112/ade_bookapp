from dataclasses import dataclass
import book_query
from pydantic import BaseModel, validators

@dataclass
class Book(BaseModel):
    # id:int
    title: str
    description: str
    content: str
    image_url: str

    def create_book(self) -> str:
        book_query.create_book(self)
        return "Book Created"

    def update_book(self, id) -> str:
        book_query.update_book(self, id)
        return "Book Updated"

    def delete_book(id) -> str:
        book_query.delete_book(id)
        return "Book Deleted"

    def fetch_books(self) -> str:
        rows=book_query.fetch_all_books()
        return rows


    def fetch_book(id) -> str:
        row=book_query.fetch_book(id)
        return row
     

    def search_book(title) -> str:
        rows=book_query.search(title)
        return rows
