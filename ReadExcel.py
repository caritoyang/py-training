import xlrd

# We need to create object of workbook
wk = xlrd.open_workbook("C:/Users/carol/Documents/XLRD.xlsx")

# number of sheets
print(wk.nsheets)

# move to sheet level by index
ws = wk.sheet_by_index(0) # the number of sheet between ( )
print(ws.nrows)
print(ws.ncols)

# move to sheet level by sheet name
ws = wk.sheet_by_name("Sheet1")

# pick data from a cell (row, col)
wc = ws.cell(2,1)
print(wc.value)

# =============================================

# Create a sheet object
ws = wk.sheet_by_name("Sheet1")
n = ws.nrows
c = ws.ncols

# Run a loop for number of rows
for i in range(0,n):
    for j in range (0,c):
        wc = ws.cell(i,j)
        print(wc.value)


# =============================================
