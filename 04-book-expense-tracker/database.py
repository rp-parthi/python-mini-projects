import sqlite3
DB_NAME = "tracker.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialise_database():
    """Creates database tables using schema.sql"""
    with get_connection() as conn:
        with open("schema.sql", "r") as schema_file:
            conn.executescript(schema_file.read())


