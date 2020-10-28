# range(start, stop, step)

#increment
for i in range(1,11,2):
    print(i)

#decrement
for i in range(10,0,-1):
    print(i)

#list
list=[1,3,5,7,10,20]
z=0
for i in list:
    z=z+i

print("Sum is: " + str(z))

# break statement
for i in range(1,11):
    if(i==5):
        break
    print(i)