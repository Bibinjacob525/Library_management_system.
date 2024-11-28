from db_connection import create_connection


def add_book(title, author, publisher, genre, year, copies):
    connection = create_connection()  # calls a function cc
    cursor = connection.cursor()   # to execute sql queries

    query = """
    INSERT INTO Books (title, author, publisher, genre, year_published, copies_available)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (title, author, publisher, genre, year, copies)
    cursor.execute(query, data)

    connection.commit()     # commit the transaction changes will be permanent
    cursor.close()
    connection.close()


def fetch_books():          # retrieve and return all book records from db
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM Books"
    cursor.execute(query)
    books = cursor.fetchall()

    cursor.close()
    connection.close()

    return books
