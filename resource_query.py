# from app import delete, fetch, update
import psycopg2
import uuid
from db import connection, cursor, create_tables
from dataclasses import dataclass
import psycopg2.extras


@dataclass
class Reources():
    author: str
    title: str    
    image_url: str
    link: str


def create_res(res:Reources):
    author = res.author
    title = res.title
    image_url = res.image_url
    link = res.link

    """ INSERT """
    try:
        insert_query = f"INSERT INTO resources (author_name, title, image_url, link) VALUES ('{author}','{title}','{image_url}','{link}')"
        cursor.execute(insert_query)
        connection.commit()
        return ({"message":"inserted succesfully"})
    except Exception as e:
        return str(e)
def update_res(res:Reources):
    author = res.author
    title = res.title
    image_url = res.image_url
    link = res.link
    try:
        update_query=f"UPDATE resources SET title='{title}', author_name='{author}', link='{link}', image_url='{image_url}' WHERE id='{id}' "
        cursor.execute(update_query)
        connection.commit()
        return ({"message":"updated succesfully"})
    except Exception as e:
        return str(e)
def delete_res(id):
    try:
        select_query=f"SELECT * FROM resources WHERE id={id}"
        cursor.execute(select_query)
        d=cursor.fetchone()
        if d is None:
            return ({"message":"id does not exist"})
        else:           
            cursor.execute('DELETE FROM resources WHERE id=%s',(id))
            connection.commit()
            return ({"message":"deleted succesfully"})
    except Exception as e:
        return e.message
def fetch_res():
    with connection as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
             c="""SELECT * FROM resources"""
             cursor.execute(c)
             rows=cursor.fetchall()
             return (rows)

def search_res(title):
    with connection as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                select_query=f"SELECT * FROM resources WHERE title LIKE '{title}'"
                cursor.execute(select_query)
                rows=cursor.fetchall()                    
                if rows is None:
                    return "search not found"
                else:
                    return (rows)