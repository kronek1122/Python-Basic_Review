from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

class PdfFileSplitter:

    def __init__(self, pdf_path):
        self.pdf_reader = PdfFileReader(pdf_path)

        self.writer1 = None
        self.writer2 = None

    def split(self, breakpoint):
        
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()

        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)
        
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, filename):
        with Path(filename+'_1.pdf').open(mode='wb') as outputfile:
            self.writer1.write(outputfile)
        with Path(filename+'_2.pdf').open(mode='wb') as outputfile:
            self.writer2.write(outputfile)

pdf_splitter = PdfFileSplitter(Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'Pride_and_Prejudice.pdf')
pdf_splitter.split(breakpoint=124)
pdf_splitter.write('split')