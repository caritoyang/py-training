import xlrd
import xlwt

# We need to create object of workbook
wk = xlrd.open_workbook("C:/Users/carol/Documents/XLRD.xlsx")
ws = wk.sheet_by_name("Sheet1")
n = ws.nrows
c = ws.ncols


wk1 = xlwt.Workbook()
ws1 = wk1.add_sheet('Testing')

# Run a loop for number of rows
for i in range(0,n):
    for j in range (0,c):
        wc = ws.cell(i,j)
        ws1.write(i,j, wc.value)

# save workbook
wk1.save('test.xls')