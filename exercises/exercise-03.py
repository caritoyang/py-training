num=int(input("Your number: "))

if(num%5==0 and num%11==0):
    print("Divisible by both.")
elif(num%5==0 or num%11==0):
    if(num%5==0):
        print("Divisible by 5 only.")
    else:
        print("Divisible by 11 only.")
else:
    print("Not divisible.")