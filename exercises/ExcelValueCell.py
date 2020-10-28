import xlrd

# We need to create object of workbook
wk = xlrd.open_workbook("C:/Users/carol/Documents/XLRD.xlsx")

# We need to create object of workbook
ws = wk.sheet_by_name("Sheet1")
n = ws.nrows
c = ws.ncols

# Run a loop for number of rows
for i in range(0,n):
    for j in range (0,c):
        wc = ws.cell(i,j)
        print(wc.value + ' ' + str(i) + ' ' + str(j))