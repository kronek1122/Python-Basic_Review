from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'zen.pdf')

pdf = PdfFileReader(str(pdf_path))

print(pdf.getNumPages())

for page in pdf.pages:
    print(page.extract_text())