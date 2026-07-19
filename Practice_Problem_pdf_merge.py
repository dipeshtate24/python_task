import os
from pypdf import PdfWriter

merger = PdfWriter()

folder_path = r'C:\Users\Dipesh\Documents\Educational book & PDF\Dipesh doc\EaseMyAI_payment_slip\last_3_month_salary'

merger = PdfWriter()

for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, file)
        merger.append(pdf_path)

with open("last_3_months_salary.pdf", "wb") as output:
    merger.write(output)

merger.close()