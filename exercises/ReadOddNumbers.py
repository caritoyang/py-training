obj = open("C:/Users/carol/Documents/PY.txt","r")

s=obj.readline()
count=0
while(s):
    if(count%2==0):
        print(s)
    s = obj.readline()
    count+=1
