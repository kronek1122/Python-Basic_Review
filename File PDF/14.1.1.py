from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'Pride_and_Prejudice.pdf')

pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = Path.home() / 'Pride_and_Prejudice.txt'

with output_file_path.open(mode='w') as output_file:
    title = pdf_reader.documentInfo.title
    num_pages = pdf_reader.getNumPages()
    output_file.write(f"{title}\nNumber of pages:{num_pages}\n\n")

    for page in pdf_reader.pages:
        text = page.extractText()
        output_file.write(text)
