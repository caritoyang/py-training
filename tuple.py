# In tuple we can't increase or decrease the size
# We can't change any value

tuple1=(45,'Testing', 'www.kinusolutions.com',23.4, 45)
tuple2=(100,200)
print(tuple1[2])

print(len(tuple1))

# Count
print(tuple1.count(45))


# Find index
print(tuple1.index("www.kinusolutions.com"))


# Merge 2 Tuple
tuple3=tuple1+tuple2
print(tuple3)


# Display all values of the tuple
for i in tuple1:
    print(i)

# Other way to display all values
i=len(tuple1)
for i in range (0,i):
    print(tuple1[i])