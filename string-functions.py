text='   This is KinuSolutions New Entrepeneurship   '

# Fetch length of String
print(len(text))
print(text[len(text)-1])

# Convert my String to Uppercase
print(text.upper())

# Convert to Lowercase
print(text.lower())

# First letter to Capital
print(text.capitalize())

# Remove blank spaces
print(len(text.rstrip())) # from right
print(len(text.lstrip())) # from left
print(len(text.strip())) # from both

# replace find split
print(text.replace("New","Best"))

# Find how many 'e' exist in the String
count=0
for i in text:
    if(i=='e'):
       count=count+1

print("The letter E appears: " + str(count) + " times.")

x=len(text)
y=len(text.replace('e',''))
print(x-y)

# Find if a word exist: -1 means not exists, if it's find it would return the index
a='New'
print(text.find(a))

list=text.split(" ")
print("Spaces in the sentence: " + str(len(list)))
print(list)

for i in list:
    if(i=="KinuSolutions"):
        print("\nFound")

# Compare string with or without case sensitive
m="Testing"
n="  testing  "

if(m.strip().upper()==n.strip().upper()):
    print("\nCompared")
else:
    print("\nNot Compared")



# Reverse my String
s="Testing this string"
t=""
l=len(s)

for i in range((l-1),-1,-1):
    print(s[i])
    t=t+s[i]

print(t)
