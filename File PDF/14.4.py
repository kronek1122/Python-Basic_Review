from PyPDF2 import PdfFileMerger
from pathlib import Path


reports_dir = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'expense_reports')

pdf_merger = PdfFileMerger()

#Pdf append
'''
expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()

for path in expense_reports:
    pdf_merger.append(str(path))

with Path('expense_reports.pdf').open(mode='wb') as output_file:
    pdf_merger.write(output_file)
'''

report_dir = (Path.home()/ 'python-basics-exercises-master' 
/ 'ch14-interact-with-pdf-files' 
/ 'practice_files'
/ 'quarterly_report')

report_path = report_dir/'report.pdf'
toc_path = report_dir/'toc.pdf'

pdf_merger.append(str(report_path))
pdf_merger.merge(1, str(toc_path))

with Path('full_report.pdf').open(mode='wb') as output_file:
    pdf_merger.write(output_file)