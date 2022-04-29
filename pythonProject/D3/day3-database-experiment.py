import sqlite3  # import sqlite library

dbc = sqlite3.connect("peoples.db") # connect to database (creates if it doesn't exist
cursor = dbc.cursor() # get a cursor

# create table... if it doesnt already exist
sql = "create table if not exists people (firstname text, lastname text, address text, town text)"
cursor.execute(sql)
dbc.commit()

sql = "insert into people values('bob', 'smith', '1 Main Street', 'Anyville')"
cursor.execute(sql)
dbc.commit()

sql = "insert into people values('jane', 'smttith', '54 Main Street', 'Anyville')"
cursor.execute(sql)
dbc.commit()

# query data from table
sql = "select firstname, lastname from people where town ='Anyville'"
cursor.execute(sql)

# get the data back to this program
data =cursor.fetchall()
print(data)

# loop around the returned data and print
for person in data:
    print(person[1])


dbc.close()

## use 33 for a test on excell data