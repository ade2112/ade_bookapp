import psycopg2
connection = psycopg2.connect( user="postgres", password="karimojid", host="localhost", port="5432", database="book_app")
cursor = connection.cursor()

def create_tables():

#Creating table as per requirement

    command = """CREATE TABLE if not exists resources (
            id serial primary key,
            author_name varchar(100) not null,
            title varchar(100) not null,
            image_url text not null,
            link text not null
            
    )"""
    
    
    try:
        
        cursor.execute(command)
        # commit the changes
        connection.commit()
        # close communication with the PostgreSQL database server
        cursor.close()
        print("table created")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
# create_tables()