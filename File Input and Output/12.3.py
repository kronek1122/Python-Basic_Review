from pathlib import Path

new_dir = Path.home()/"new_directory"
new_dir.mkdir(exist_ok=True)

nested_dir = new_dir / 'folder_a' / 'folder_b'
nested_dir.mkdir(parents=True, exist_ok=True)

new_dir.exists()
new_dir.is_dir()

file_path = new_dir/ "file1.txt"
file_path.touch()


for path in new_dir.glob('*.txt'):
    print(path)

#print(list(new_dir.iterdir()))
paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
]

'''
for path in paths:
    path.touch()
    '''

#print(list(new_dir.glob('**/*.py')))

#print(list(new_dir.rglob('*.py')))


# Moving a file or folder
'''
source = new_dir / 'file1.txt'
destination = new_dir / 'folder_a' / 'file1.txt'
if not destination.exists():
    source.replace(destination)
'''

# Rename a directory
'''
source = new_dir / 'folder_c'
destination = new_dir / 'folder_d'
source.replace(destination)
'''

# Delete a file
file_path = new_dir / 'program1.py'
file_path.unlink(missing_ok=True)

# Delete path over directory and remove directory
folder_d = new_dir / "folder_d"
for path in folder_d.iterdir():
    path.unlink()

folder_d.rmdir()

