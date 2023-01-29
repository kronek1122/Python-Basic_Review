import sqlite3


create_table = '''
DROP TABLE IF EXISTS Roster;
CREATE TABLE Roster(
    Name TEXT,
    Species Text,
    Age INT
);'''
populate_values = (
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
)

with sqlite3.connect('Roster.db') as connection:
    cursor = connection.cursor()
    cursor.executescript(create_table)
    cursor.executemany("INSERT INTO Roster VALUES(?,?,?)",populate_values)

with sqlite3.connect('Roster.db') as connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE Roster SET Name=? WHERE Species=? AND AGE=?;",('Ezri Dax','Trill',300))
    result = cursor.execute('SELECT Name, Species, Age FROM Roster WHERE Species = "Bajoran"')
    for row in result.fetchall():
        print(row)
   