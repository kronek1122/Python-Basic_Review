from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path


pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'ugly.pdf')

# first option (rotate when you now what page are rotated)
pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path('ugly_rotated.pdf').open(mode = 'wb') as output_file:
    pdf_writer.write(output_file)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

#option 2: rotate wit /Rotate key value
for page in pdf_reader.pages:
    if page['/Rotate']  == -90:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path('ugly_rotated2.pdf').open(mode = 'wb') as output_file:
    pdf_writer.write(output_file)


