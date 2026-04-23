import os
os.chdir(os.path.dirname(__file__))

from pypdf import PdfWriter

writer = PdfWriter()

pdfs = ["Aicte.pdf","EMF.pdf"]
for pdf in pdfs:
    writer.append(pdf)

writer.write("merged.pdf")
writer.close()