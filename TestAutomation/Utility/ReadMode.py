# MODES (r-read, w-write, a-append, r+ read&write, w+ write&read, a+ append&read

# Open file for reading
obj = open("C:/Users/carol/Documents/PY.txt","r")

# Read all data from the file
# print(obj.read())

# Read 1 line from the file
# print(obj.readline())
# print(obj.readline())

# Read onyl few characters from file
# print(obj.read(10))

# Read all chars from file and display 1 by 1
# for i in obj.read():
#     print(i)

# Read all data from file line by line
s=obj.readline()
while(s):
    print(s)
    s = obj.readline() # change the line, if not, it will enter in a loop reading the 1st line