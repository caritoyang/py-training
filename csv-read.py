import csv

# open file to read data
f = open('C:\\Users\\carol\\Documents\\data11.csv')

# render the file into csv format
csv_data = csv.reader(f)
list1 = list(csv_data)
print(list1)

for row in list1:
    l = len(row)
    for j in range(0,l):
        print(row[j])

l = len(list1)

for i in range(0,l):
    print(list1[i][0])
    print(list1[i][1])
    print(list1[i][2])