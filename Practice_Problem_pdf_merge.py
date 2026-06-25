import os
from pypdf import PdfWriter

merger = PdfWriter()

folder_path = 'pdf_folder'

for files in os.listdir(folder_path):
    if files.endswith('.pdf'):
        
        for pdf in files :
            merger(pdf)

merger.write("new_file.pdf")
