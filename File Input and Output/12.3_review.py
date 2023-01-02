from pathlib import Path
import shutil

new_dir = Path.home()/"my_folder"
new_dir.mkdir(exist_ok=True)

paths = [
    new_dir / 'file1.txt',
    new_dir / 'file2.txt',
    new_dir / 'image1.png',
]

for path in paths:
    path.touch()

source = new_dir / 'image1.png'
destination = new_dir / 'images' 
destination.mkdir(exist_ok=True)
destination = new_dir / 'images'/ 'image1.png'


if not destination.exists():
    source.replace(destination)


file_path = new_dir / 'file1.txt'
file_path.unlink(missing_ok=True)


shutil.rmtree(new_dir)

