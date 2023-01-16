from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'Pride_and_Prejudice.pdf')

input_pdf = PdfFileReader(str(pdf_path))

pdf_writer1 = PdfFileWriter()


for n in range(0,150):
    page = input_pdf.getPage(n)
    pdf_writer1.addPage(page)

with Path('part_1.pdf').open(mode='wb') as outputfile:
    pdf_writer1.write(outputfile)

pdf_writer2 = PdfFileWriter()

for n in range(151,input_pdf.getNumPages()):
    page = input_pdf.getPage(n)
    pdf_writer2.addPage(page)

with Path('part_2.pdf').open(mode='wb') as outputfile:
    pdf_writer2.write(outputfile)
