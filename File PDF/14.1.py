from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'Pride_and_Prejudice.pdf')

pdf = PdfFileReader(str(pdf_path))


#print(pdf.getNumPages())
#print(pdf.documentInfo.title)

first_page = pdf.getPage(0)

for page in pdf.pages:
    print(page.extract_text())