# excel_exporter.py

from openpyxl import Workbook
from openpyxl.styles import Font
from io import BytesIO

def generate_excel_with_formulas(df):
    wb = Workbook()
    ws = wb.active
    ws.title = "Pricebook"

    # Add headers
    headers = ["Service", "Category", "Labor Cost", "Material Cost", "Price", "Total Cost", "Profit Margin (%)"]
    ws.append(headers)

    for idx, row in df.iterrows():
        excel_row = idx + 2  # Header is row 1
        ws.append([
            row['Service'],
            row['Category'],
            row['Labor Cost'],
            row['Material Cost'],
            row['Price'],
            f"=C{excel_row}+D{excel_row}",  # Total Cost = Labor + Material
            f"=(E{excel_row}-F{excel_row})/E{excel_row}"  # Profit Margin
        ])

    for cell in ws[1]:
        cell.font = Font(bold=True)

    stream = BytesIO()
    wb.save(stream)
    stream.seek(0)
    return stream
