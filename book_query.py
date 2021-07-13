import psycopg2
import uuid
from dataclasses import dataclass


connection = psycopg2.connect(user="postgres",
                                  password="",
                                  host="localhost",
                                  port="5432",
                                  database="book_app")
cursor = connection.cursor()

@dataclass
class Book():
    title: str
    description: str
    content: str
    image_url: str


def create_book(book: Book):
    id = uuid.uuid4()
    title = book.title
    description = book.description
    content = book.content
    image_url = book.image_url

    """ INSERT """
    insert_query = f"INSERT INTO book (id, title, description, content, image_url) VALUES ('{id}','{title}','{description}','{content}', '{image_url}')"
    cursor.execute(insert_query)
    connection.commit()
    return "Insert was successful"


def update_book(book: Book):
    pass

def delete_book(id):
    pass

def fetch_all_books():
    pass

def fetch_book(id):
    pass

def search(name):
    pass

def add_to_favorite(id):
    pass