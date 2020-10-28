import xlwt

# create object of Workbook

wk = xlwt.Workbook()
ws = wk.add_sheet('Testing')
ws.write(0,0,'KinuSolutions') # row, colum, value
ws.write(1,0,'www.kinusolutions.com')

# save workbook
wk.save('test.xls')
