import sqlite3
from player import Player

# conn = sqlite3.connect('players.db') # Connection to the local database
# Connection to memory database, so it will refresh and clear every run
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE players(
            first text,
            last text,
            age integer
            )""")

# c.execute("INSERT INTO players VALUES ('Andresinho', 'Gaucho', '29')") # Insert values in DB
# c.execute("DELETE FROM players WHERE first='Chris'") # Delete values from DB
# c.execute("SELECT * FROM players WHERE last = 'Jhonson'") # Query to search values in DB
# print(c.fetchall())

pla_1 = Player('Mark', 'Hoppus', 35)
pla_2 = Player('Travis', 'Barker', 25)

print(pla_1.first)
print(pla_1.last)
print(pla_1.age)

# # first way to insert Python objects in DB using placeholders - tuple
# c.execute("INSERT INTO players VALUES (?, ?, ?)",
#           (pla_1.first, pla_1.last, pla_1.age))
# conn.commit()

# # second way to insert Python objects in DB using placeholders - dictionary
# c.execute("INSERT INTO players VALUES (:first, :last, :age)", {
#           'first': pla_2.first, 'last': pla_2.last, 'age': pla_2.age})
# conn.commit()

# # first way to search in DB using placeholders - tuple
c.execute("SELECT * FROM players WHERE last = ?", ('Jhonson',))
print(c.fetchall())

# # second way to search in DB using placeholders - dictionary
c.execute("SELECT * FROM players WHERE last = :last", {'last': 'Barker'})
print(c.fetchall())

conn.commit()

conn.close()
