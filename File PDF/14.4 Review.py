from PyPDF2 import PdfFileMerger
from pathlib import Path


#first part concatenated 2 files
merge_dir = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files')

pdf_merger = PdfFileMerger()

pdf_merger.append(merge_dir/'merge1.pdf')
pdf_merger.append(merge_dir/'merge2.pdf')

with Path('concatenated.pdf').open(mode='wb') as output_file:
    pdf_merger.write(output_file)

#part two merge file 3 to concatenated.pdf

pdf_merger1 = PdfFileMerger()

pdf_merger1.append('concatenated.pdf')
pdf_merger1.merge(1,merge_dir/'merge3.pdf')

with Path('merged.pdf').open(mode='wb') as output_file:
    pdf_merger1.write(output_file)