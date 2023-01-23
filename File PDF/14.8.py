from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import red, blue 


canvas = Canvas('hello.pdf', pagesize=LETTER)

canvas.setFont('Times-Roman', 18)
canvas.setFillColor('red')
canvas.drawString(1*inch ,1*inch , "Hello World (Times New Roman 18pt)")

canvas.setFont('Courier-Bold', 12)
canvas.setFillColor('blue')
canvas.drawString(1*cm ,1*cm , "Hello World (Courier 12pt)")

canvas.save()
