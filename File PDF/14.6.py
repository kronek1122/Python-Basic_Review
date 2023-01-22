from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

#encripting
pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'newsletter.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_password='SuperSecret', owner_password="Admin")

with Path('newsletter_protected.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)

#decripting
pdf_path = ('newsletter_protected.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_reader.decrypt(password="Admin")
pdf_writer = PdfFileWriter()

pdf_reader.getPage(0)