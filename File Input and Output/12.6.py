
from pathlib import Path

'''
temperature_readings = [68, 65, 68, 70, 74, 72]

path = Path.home()/ 'temperature.txt'

with path.open(mode='w', encoding='utf-8') as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")

with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()

temperature = text.split(',')

print(temperature)

#list comprehension

int_temperature = [int(temp) for temp in temperature]

print(int_temperature)
'''


#write using imort csv
import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
    ]

file_path = Path.home()/ 'temperature.csv'
with file_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures)

with file_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]

    daily_temperatures.append(int_row)

print(daily_temperatures)

def process_row(row):
    row['salary'] = float(row['salary'])
    return row

file_path = Path.home()/ 'employees.csv'
with file_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(process_row(row))

people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24},
    ]

file_path = Path.home() / 'people.csv'
with file_path.open(mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writerows(people)