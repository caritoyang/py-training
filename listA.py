list1=[34,43.22,"Testing",55,89,"World"]

# Fetching by index
print(list1[1])

# Rage of index
print(list1[1:4])

# Starting index only
print(list1[2:])

# End index only
print(list1[:4])

# Replace by index
list1[3]=100
print(list1[3])

# Add items
list1.insert(3,"ABCD")
print(list1)

# Delete item
list1.remove("Testing")
print(list1)

list1=[34, 43.22, "Testing", 55, 89, "World", 55]
list2=[34, 43.22, "Testing", 55, 89, "World", 55]
list3=list1+list2

list1.insert(4,"www.kinusolutions.com")

print(list3)