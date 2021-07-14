from app import delete, fetch, update
import psycopg2
import uuid
from db import connection, cursor, create_tables
from dataclasses import dataclass
import psycopg2.extras




@dataclass
class Book():
    title: str
    description: str
    content: str
    image_url: str


def create_book(book: Book):
    title = book.title
    description = book.description
    content = book.content
    image_url = book.image_url

    """ INSERT """
    try:
        insert_query = f"INSERT INTO book (title, description, contents, image_url) VALUES ('{title}','{description}','{content}','{image_url}')"
        cursor.execute(insert_query)
        connection.commit()
        return "Insert was successful"
    except Exception as e:
        return str(e)

def update_book(book: Book,id):
    title = book.title
    description = book.description
    content = book.content
    image_url = book.image_url
    update_query=f"UPDATE book SET title='{title}', description='{description}', contents='{content}', image_url='{image_url}' WHERE id='{id}' "
    cursor.execute(update_query)
    connection.commit()
    return "Update was succesfull"

def delete_book(id):
    try:
        select_query=f"SELECT * FROM book WHERE id={id}"
        cursor.execute(select_query)
        d=cursor.fetchone()
        if d is None:
            print("no id")
            return ({"message":"id does not exist"})
        else:           
            cursor.execute('DELETE FROM book WHERE id=%s',(id))
            connection.commit()
            return ({"message":"deleted succesfully"})
    except Exception as e:
        return e.message

def fetch_all_books():
    with connection as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
             c="""SELECT * FROM book"""
             cursor.execute(c)
             rows=cursor.fetchall()
             return (rows)

def fetch_book(id):
    with connection as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                select_query=f"SELECT * FROM book WHERE id={id}"
                cursor.execute(select_query)
                rows=cursor.fetchone()
                if rows is None:
                    return "id does not exist"
                else:
                    return (rows)

def search(title):
     with connection as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                select_query=f"SELECT * FROM book WHERE title LIKE '{title}'"
                cursor.execute(select_query)
                rows=cursor.fetchall()                    
                if rows is None:
                    return "search not found"
                else:
                    return (rows)
    


