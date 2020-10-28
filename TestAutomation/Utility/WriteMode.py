# Create a file and write
obj = open("C:/Users/carol/Documents/PY1.txt","w")

obj.write("Hello! This is New Python File")
obj.close()


# Open a file and add new data
obj = open("C:/Users/carol/Documents/PY1.txt","a")
obj.write("\n Add a new line.")
obj.close()