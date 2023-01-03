from pathlib import Path

# Reading data
path = Path.home() / 'hello.txt'
path.touch()
with path.open(mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end="")

# Writing Data (overwritten)
with path.open(mode='w', encoding='utf-8') as file:
    file.write('Hi there!')

# Writing Data (multiple lines)
lines_of_text = [
    "Hello from Line 1\n",
    "Hello from Line 2\n",
    "Hello from Line 3\n",
]
with path.open(mode='w', encoding='utf-8') as file:
    file.writelines(lines_of_text)

# Writing Data (append)
with path.open(mode='a', encoding='utf-8') as file:
    file.write('\nHello')