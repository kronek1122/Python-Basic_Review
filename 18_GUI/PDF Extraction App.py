import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

input_path = gui.fileopenbox(title='Select a PDF to open',
                        default='*.pdf')

if input_path is None:
    exit()

input_file = PdfFileReader(input_path)
total_page = input_file.getNumPages()

start_page = gui.enterbox(msg='Select a start page to extraction',
                                title = "Choose page...")

if start_page is None:
    exit()

while(
    not start_page.isdigit()
    or int(start_page) < 0
    or int(start_page) > total_page
):
    gui.msgbox(msg='Page numbers must be positive', title='Invalid page!')
    start_page = gui.enterbox(msg='Select a start page to extraction',
                                title = "Choose page...")
    if start_page is None:
        exit()

start_page = int(start_page)

end_page = gui.enterbox(msg='Select a end page to extraction',
                                title = "Choose page...")

if end_page is None:
    exit()

while(
    not end_page.isdigit()
    or int(end_page) < 0
    or int(end_page) > total_page
    or int(end_page) < int(start_page)
):
    gui.msgbox(msg='Try input valid page number', title='Invalid page!')
    end_page = gui.enterbox(msg='Select a end page to extraction',
                                title = "Choose page...")
    if end_page is None:
        exit()

end_page = int(end_page)

save_title = 'Save the extrated PDF as...'
file_typ = "*.pdf"
output_path = gui.filesavebox(title = save_title, default=file_typ)

if output_path is None:
        exit()

while input_path == output_path:
    gui.msgbox(msg = 'Cannot overwrite orginal file!')
    output_path = gui.filesavebox(title = save_title, default=file_typ)
    if output_path is None:
        exit()

output_pdf = PdfFileWriter()

for n in range(start_page-1, end_page):
    page = input_file.getPage(n)
    output_pdf.addPage(page)

with open(output_path, 'wb') as output_file:
    output_pdf.write(output_file)