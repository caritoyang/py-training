obj = open("C:/Users/carol/Documents/PY.txt","r")

obj2 = open("C:/Users/carol/Documents/PY3.txt","w")
obj2.write(obj.read().upper())
obj.close()