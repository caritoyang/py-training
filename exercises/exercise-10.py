# Factorial

number=int(input("Please select a number: "))

for i in range(number-1,0,-1):
    number=number*i

print(number)