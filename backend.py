import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER,
        isbn INTEGER)""")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("""INSERT INTO book VALUES
        (NULL,?,?,?,?)""",
        (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("""SELECT * FROM book WHERE
        title=? OR
        author=? OR
        YEAR=? OR
        ISBN=?""", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE ID=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("""UPDATE book SET
        title=?,
        author=?,
        year=?,
        isbn=?
        WHERE id=?""",
        (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
update(7,"The Galaxy","Peter Jason Qull", 1982, 645123879)
#delete(5)
#print(view())
#print(search(title="The Sun"))
#update(11, 'Its all my fault', 'Chris Mistaker', 2018, 783681461)
