import os
from pypdf import PdfWriter

merger = PdfWriter()

folder_path = 'pdf_folder'

for pdf in os.listdir(folder_path):
    merger(pdf)

merger.write("new_file.pdf")
