obj = open("C:/Users/carol/Documents/PY.txt","r")

num=int(input("how many lines? "))
s=obj.readline()

for i in range(0,num):
    s = obj.readline()
    print(s)
