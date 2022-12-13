import	sqlite3

conn	=	sqlite3.connect("test_databace.db")
cur = conn.cursor()

cur.execute("select * from idiotis")

