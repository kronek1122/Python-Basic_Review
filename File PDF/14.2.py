from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'Pride_and_Prejudice.pdf')

input_pdf = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_reader = PdfFileReader()
pdf_writer.addPage(first_page)

with Path('first_page.pdf').open(mode='wb') as outputfile:
    pdf_writer.write(outputfile)

for n in range(1,4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)

with Path('Chapter1.pdf').open(mode='wb') as outputfile:
    pdf_writer.write(outputfile)
