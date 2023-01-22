from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

#encripting
pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'scrambled.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

page_order =[]

for page in pdf_reader.pages:
    text = page.extractText()
    page_order.append(text[0])


for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_order.index(str(n+1)))
    page.rotateCounterClockwise(int(page['/Rotate']))
    pdf_writer.addPage(page)


with Path('unscrambled.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)

