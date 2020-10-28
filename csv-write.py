import csv

# open file, w=writable mode, newline = everytime we write, it will go to a new line
f = open('C:\\Users\\carol\\Documents\\data22.csv','w',newline='')
csv_v = csv.writer(f)
csv_v.writerow(['hello0',11,99])
csv_v.writerow(['hello1',12,98])
csv_v.writerow(['hello2',13,97])
csv_v.writerow(['hello3',14,96])

# save and close
f.close()