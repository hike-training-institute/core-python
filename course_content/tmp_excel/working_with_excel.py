from openpyxl import load_workbook
wb = load_workbook(filename='bank_accounts.xlsx')
sheet = wb.active
cols = ['A', 'B', 'C']
for col in cols:
    for i in range(1, 100):
        address = col + str(i)
        value = sheet[address].value
        if value is None:
            break
        print(value)