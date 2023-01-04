from pathlib import Path
import csv

numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    ]

num = []
path = Path.home() / 'numbers.csv'

with path.open(mode='w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(numbers)

with path.open(mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        num.append(int_row)
    print(num)


favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
    ]
fav = []
path = Path.home() / 'favorite_color.csv'
with path.open(mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['name', "favorite_color"])
    writer.writerows(favorite_colors)

with path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, fieldnames=['name', "favorite_color"])
    for row in reader:
        fav.append(row)
    print(fav)