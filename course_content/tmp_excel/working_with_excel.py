from openpyxl import load_workbook
wb = load_workbook(filename='bank_accounts.xlsx')
# sheet = wb.get_sheet_by_name('Sheet2')
sheet = wb.active

# print(sheet['B3'].value)
#
# #
# cols = ['A']#, 'B', 'C']
# for col in cols:
#     for i in range(1, 100):
#         address = col + str(i)
#         value = sheet[address].value
#         if value is None:
#             break
#         print(value)

sheet['B3'] = 20000
wb.save('bank_accounts.xlsx')