from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host="sql12.freesqldatabase.com",
            database="sql12619725",
            user="sql12619725",
            password="Rke8KqezCl",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.Error as e:
        print(e)
    return conn


@app.route("/books", methods=["GET", "POST"])
def book():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM book")
        books = [
            dict(
                id=row["id"],
                author=row["author"],
                language=row["language"],
                title=row["title"],
            )
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    if request.method == "POST":
        new_auth = request.form["author"]
        new_language = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO book(author, language, title)
            VALUES(%s,%s,%s)
            """
        cursor.execute(sql, (new_auth, new_language, new_title))
        conn.commit()
        return f"book with id: {cursor.lastrowid} created successfully"


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = sqlite3.connect("book.sqlite")
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book)
        else:
            return "Something Wrong", 404

    if request.method == "PUT":
        sql = """UPDATE book
                SET title=%s,
                author=%s,
                language=%s,
                WHERE id=%s
        """
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]

        cursor.execute(sql, (title, author, language, id))
        conn.commit()

        cursor.execute("SELECT * FROM book WHERE id=%d", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book)
        else:
            return "Something Wrong", 404

    if request.method == "DELETE":
        sql = """DELETE FROM book WHERE id = %d"""
        cursor.execute(sql, (id,))
        conn.commit()
        return f"The book with id: {id} has been deleted"


if __name__ == "__main__":
    app.run(debug=True)
