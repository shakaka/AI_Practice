import openpyxl

from openpyxl.style import Font

wb=openpyxl.Workbook()
sheet = wb.get_sheet_by_name('sheet')
italic24Font=Font(size=24,italic=True)
sheet['A1'].font=italic24Font
sheet['A1']='hello'
wb.save('')
