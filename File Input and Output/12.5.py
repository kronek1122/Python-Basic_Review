from pathlib import Path

path = Path.home() / 'hello.txt'
path.touch()
file = path.open(mode='r', encoding='utf-8')

file.close()

file_path = 'C/Users/kronk/hello.txt'

file = open(file_path, mode='r', encoding='utf-8')

file.close()