import sqlite3
from player import Player

# conn = sqlite3.connect('players.db') # Connection to the local database
# Connection to memory database, so it will refresh and clear every run
conn = sqlite3.connect(':memory:')

c = conn.cursor()

# Creates table in the database
c.execute("""CREATE TABLE players( 
            first text,
            last text,
            age integer
            )""")

# Functions for INSERT, SELECT, UPDATE and DELETE to/from DATABASE


def insert_pla(pla):  # Insert given player to DB
    with conn:  # Context Manager -> commits auto/ and if it fail it will roll it back
        c.execute("INSERT INTO players VALUES (:first, :last, :age)", {
            'first': pla.first, 'last': pla.last, 'age': pla.age})


def get_all_pla():  # Search for all players in DB
    c.execute("SELECT * FROM players")
    return c.fetchall()


def get_pla_by_name(lastname):  # Search player by lastname
    c.execute("SELECT * FROM players WHERE last = :last", {'last': lastname})
    return c.fetchall()


def update_age(pla, age):  # Update the age of a given player
    with conn:
        c.execute("UPDATE players SET age = :age WHERE first= :first AND last = :last", {
                  'first': pla.first, 'last': pla.last, 'age': age})


def remove_pla(pla):  # Remove a player from DB
    with conn:
        c.execute("DELETE from players WHERE first=:first AND last = :last", {
                  'first': pla.first, 'last': pla.last})


# Create some players from the Class Player and then we can insert them in the DB
pla_1 = Player('Mark', 'Hoppus', 35)
pla_2 = Player('Travis', 'Barker', 25)

insert_pla(pla_1)
insert_pla(pla_2)

plas = get_all_pla()
print(plas)

update_age(pla_2, 30)
remove_pla(pla_1)

plas = get_pla_by_name('Barker')
print(plas)

conn.close()

