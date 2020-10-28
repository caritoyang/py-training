obj1 = open("C:/Users/carol/Documents/PY.txt","r")
obj2 = open("C:/Users/carol/Documents/PY1.txt","r")
obj3 = open("C:/Users/carol/Documents/PY2.txt","a")


obj3.write(obj1.read()+"\n" + obj2.read())
obj3.close()