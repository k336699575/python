import openpyxl

  
wb = openpyxl.load_workbook('names_and_savings.xlsx')

ws = wb['工作表1']

results = 1

for row in ws.iter_rows():
    numbers: int =row[2].value
    if numbers >= 20000:
        ws.cell(row=results, column=4).value ="VIP"
    results += 1    
# print(ws.cell(row=1, column=1).value)
# print(ws.cell(row=1, column=2).value)
# print(ws.cell(row=1, column=3).value)

      
    wb.save('names_and_savings_new.xlsx')