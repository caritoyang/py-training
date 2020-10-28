import openpyxl

# create sheet
wk = openpyxl.Workbook()
sh = wk.active
sh.title = 'HelloKinuSolutions'

print(sh.title)

# Assign value
sh['A4'].value = 'www.kinusolutions.com'

# Create 2nd Sheet
wk.create_sheet(title='Testing')
sh1 = wk['Testing']
sh1['C4'].value = 'This is a new cell'

# Remove sheet
wk.remove(wk['HelloKinuSolutions'])

# Save the file
wk.save('PySheet.xlsx')