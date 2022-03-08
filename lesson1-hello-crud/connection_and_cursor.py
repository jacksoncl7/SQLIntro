import sqlite3

# hello!!! I'm a connection
connection = sqlite3.connect("tmp/MyBank.sqlite.db")

# cursor -  The write/read executor
cursor = connection.cursor()

# executing a query
# Explaning: This query go to create a table people if this don't exist.
cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, ammount INTEGER, kind TEXT)")

## TOSEARCH: is ammount a integer in real life? Which kind of problem there is when we are using the float type for money transactions?

# Executing other queries
# Explaning: These queries go include a new rows into people table.
cursor.execute("INSERT INTO people (name, ammount, kind) VALUES ('Billy', 1000000, 'Universitary')")
# cursor.execute("INSERT INTO people VALUES ('Gusta Analise', 100, 'Business')")
# cursor.execute("INSERT INTO people VALUES ('Gusta Analise', 100, 'Business')")
# cursor.execute("INSERT INTO people VALUES ('Gusta Analise', 100, 'Business')")

# saving changes
connection.commit()

## TOSEARCH: Can I have three people with the same name? How to turn UNIQUE my rows? What rows I can based to be  UNIQUE registry?

# Executing another queries - SELECT
rows = cursor.execute("SELECT * FROM people")
# for row in rows:
#     print(row)

# print(rows.fetchall())

# next = cursor.fetchone()
# while next != None:
#     print(next)
#     next = cursor.fetchone()


# Executing another queries - UPDATE

# Executing another queries - DELETE

# clossing your connection
connection.close()
