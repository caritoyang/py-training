obj = open("C:/Users/carol/Documents/PY.txt","r")
s=obj.readline()

while(s):
    if(s.find("error")==-1):
        print(s)
    s=obj.readline()
