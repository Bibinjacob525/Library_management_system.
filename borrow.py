from db_connection import create_connection


def borrow_book(member_id, book_id, borrow_date, return_date):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT copies_available FROM Books WHERE book_id = %s", (book_id,))
    available = cursor.fetchone()[0]

    if available > 0:
        query = """
        INSERT INTO BorrowRecords (member_id, book_id, borrow_date, return_date)
        VALUES (%s, %s, %s, %s)
        """
        data = (member_id, book_id, borrow_date, return_date)
        cursor.execute(query, data)

        cursor.execute("UPDATE Books SET copies_available = copies_available - 1 WHERE book_id = %s", (book_id,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
    else:
        cursor.close()
        connection.close()
        return False


def return_book(record_id, book_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM BorrowRecords WHERE record_id = %s", (record_id,))
    cursor.execute("UPDATE Books SET copies_available = copies_available + 1 WHERE book_id = %s", (book_id,))

    connection.commit()
    cursor.close()
    connection.close()
