from pathlib import Path

path = Path.home() / 'starships.txt'
text = []
directory_list=[
    "Discovery\n",
    'Enterprise\n',
    'Defiant\n',
    'Voyager\n',
]
with path.open(mode='w', encoding='utf-8') as file:
    file.writelines(directory_list)

with path.open(mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end='')

with path.open(mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        if line[0] == "D":
            print(line, end='')

