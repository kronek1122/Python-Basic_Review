from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

#encripting
pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'top_secret.pdf')

pdf_reader = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_password='Unguessable')

with Path('top_secret_encrypted.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)

pdf_path = ('top_secret_encrypted.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
pdf_reader.decrypt(password='Unguessable')

print(pdf_reader.getPage(0))