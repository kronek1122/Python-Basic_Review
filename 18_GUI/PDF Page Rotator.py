import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

input_path = gui.fileopenbox(title='Select a PDF to rotate',
                        default='*.pdf')

if input_path is None:
    exit()

choices = ('90', '180', '270')
degrees = gui.buttonbox(msg='Rotate the PDF clockwise by how many degrees?',
                                title = "Choose rotation...",
                                choices=choices)

if degrees is None:
    exit()

degrees = int(degrees)

save_title = 'Save the rotated PDF as...'
file_typ = "*.pdf"
output_path = gui.filesavebox(title = save_title, default=file_typ)

while input_path == output_path:
    gui.msgbox(msg = 'Cannot overwrite orginal file!')
    output_path = gui.filesavebox(title = save_title, default=file_typ)

if output_path is None:
    exit()

input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

for page in input_file.pages:
    page = page.rotateClockwise(degrees)
    output_pdf.addPage(page)

with open(output_path, 'wb') as output_file:
    output_pdf.write(output_file)