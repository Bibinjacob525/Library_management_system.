from db_connection import create_connection


def add_member(name, email, phone, start_date, end_date):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Members (name, email, phone, membership_start, membership_end)
    VALUES (%s, %s, %s, %s, %s)
    """
    data = (name, email, phone, start_date, end_date)
    cursor.execute(query, data)

    connection.commit()
    cursor.close()
    connection.close()


def fetch_members():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM Members"
    cursor.execute(query)
    members = cursor.fetchall()

    cursor.close()
    connection.close()

    return members
