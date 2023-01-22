from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import copy


pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'half_and_half.pdf')

pdf_reader = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()

first_page = pdf_reader.getPage(0)

left_side = copy.deepcopy(first_page)
current_coords = left_side.mediaBox.upperRight
new_coords = (current_coords[0]/2,current_coords[1])
left_side.mediaBox.upperRight = new_coords

right_side = copy.deepcopy(first_page)
right_side.mediaBox.upperLeft = new_coords

pdf_writer = PdfFileWriter()
pdf_writer.addPage(left_side)
pdf_writer.addPage(right_side)

with Path('crooped_pages.pdf').open(mode = 'wb') as output_file:
    pdf_writer.write(output_file)

