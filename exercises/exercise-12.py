# Check if the number is Prime

num=int(input("Please input a Number: "))
z=0

for i in range(2,num):
    if(num%i==0):
        print("This number is not Prime.")
        z=1
        break
if(z==0):
    print("This number is Prime.")
