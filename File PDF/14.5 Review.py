from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import copy

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'split_and_rotate.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    page.rotateCounterClockwise(90)
    pdf_writer.addPage(page)

with Path('rotated.pdf').open(mode = 'wb') as output_file:
    pdf_writer.write(output_file)

pdf_path = ('rotated.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()


for n in range(pdf_reader.getNumPages()):
    left_side = copy.deepcopy(pdf_reader.getPage(n))
    right_side = copy.deepcopy(pdf_reader.getPage(n))
    current_coords = left_side.mediaBox.upperRight
    new_coords = (current_coords[0]/2,current_coords[1])
    left_side.mediaBox.upperRight = new_coords
    right_side.mediaBox.upperLeft = new_coords

    pdf_writer.addPage(left_side)
    pdf_writer.addPage(right_side)

with Path('split.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)


