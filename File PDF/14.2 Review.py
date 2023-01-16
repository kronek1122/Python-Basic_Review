from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'Pride_and_Prejudice.pdf')

input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
#last_page = input_pdf.getPage(-1)
#pdf_writer.addPage(last_page)

for n in range(input_pdf.getNumPages()):
    if n % 2 == 0:
        page = input_pdf.getPage(n)
        pdf_writer.addPage(page)

with Path('every_other_pages.pdf').open(mode='wb') as outputfile:
    pdf_writer.write(outputfile)

