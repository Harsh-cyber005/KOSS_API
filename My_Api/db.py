import sqlite3
import pymysql

conn = pymysql.connect(
    host="sql12.freesqldatabase.com",
    database="sql12619725",
    user="sql12619725",
    password="Rke8KqezCl",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

cursor = conn.cursor()

sql_query = """CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
    )
"""

cursor.execute(sql_query)
