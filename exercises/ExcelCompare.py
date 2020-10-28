import xlrd

# We need to create object of workbook
wk = xlrd.open_workbook("C:/Users/carol/Documents/XLRD1.xlsx")
wk2 = xlrd.open_workbook("C:/Users/carol/Documents/XLRD2.xlsx")

ws = wk.sheet_by_name("Sheet1")
ws2 = wk2.sheet_by_name("Sheet1")
n = ws.nrows
c = ws.ncols

# Run a loop for number of rows
for i in range(0,n):
    for j in range (0,c):
        wc = ws.cell(i,j)
        wc2 = ws2.cell(i,j)
        if(wc.value != wc2.value):
            print('Mismatch in cell: ' + str(i) + ' ' + str(j))