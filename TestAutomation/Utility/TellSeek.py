# Info: https://uniwebsidad.com/libros/python/capitulo-9/metodos-del-objeto-file

# Reading data from the file
obj = open("C:/Users/carol/Documents/PY.txt","r")

print(obj.tell()) # 0
obj.readline() # Retorna la posición actual del puntero.
print(obj.tell()) # 16
obj.readline()
print(obj.tell()) # 32

obj.seek(5) # Mueve el puntero hacia el byte indicado.
print(obj.tell())