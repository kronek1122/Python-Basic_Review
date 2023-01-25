import sqlite3


with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    result = cursor.execute(query)
    row = result.fetchone()
    time = row[0]
    print(time)

#database Tables
create_table = '''
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);'''

insert_value = '''
INSERT INTO People VALUES(
    'Ron',
    'Rudy',
    42
);'''

sql = '''
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERT INTO People VALUES(
    'Ron',
    'Rudy',
    42
);'''

people_values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28)
)

'''
with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)
    cursor.execute(insert_value)

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    query = "SELECT*FROM People;"
    result = cursor.execute(query)
    print(result.fetchone())

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    #cursor.executescript(sql)
    cursor.executemany("INSERT INTO People VALUES(?,?,?)",people_values)
'''

first_name = input("Enter first name: ")
last_name = input('Enter last name: ')
age = int(input('Enter age: '))
data = (first_name, last_name, age)
query = (
    "INSERT INTO People VALUES"
    f"('{first_name}','{last_name}',{age})"
)
with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES(?,?,?);",data)
    #cursor.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",(45, 'Luigi', 'Vercotti'))
    cursor.execute(
        "SELECT FirstName, LastName FROM People WHERE AGE > 30;"
    )
    for row in cursor.fetchall():
        print(row)