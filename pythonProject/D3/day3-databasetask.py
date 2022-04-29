import sqlite3

#35 on workbook

con = sqlite3.connect("bookstest.db") # starts a db/connects to it. doesn't need .db
cur = con.cursor()

# create table
cur.execute("create table if not exists books (title text, author text)")
con.commit()

# the code above will run once, then crash.
# the following code prevents this, add if not exists to #1

#cur.execute("create table if not exists books (title text, author text)")


con.close()
# closes connection to database. all lines of code are in between connect and close


