i=1

# increment
while(i<=10):
    print(i)
    i+=1

# decrement
while(i>=1):
    print(i)
    i-=1


# Break statement
number = int(input("Please enter your number: "))
for i in range(1,11):
    if(number*i>60):
        break
    print(number*i)

# Continue Statement: skip without executing the one that is true
number = int(input("Please enter your number: "))
for i in range(1,11):
    if(number*i%10==0)
        continue
    print(number*i)

# Else statement
for i in range(1,11):
    print(i)
else:
    print("Loop ended.")