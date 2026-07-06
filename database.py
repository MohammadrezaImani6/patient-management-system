import sqlite3


def get_connection():
    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()
    return connection, cursor


def create_tables():
    connection, cursor = get_connection()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        disease TEXT,
        visit_date TEXT,
        description TEXT)""")
    connection.commit()
    connection.close()
