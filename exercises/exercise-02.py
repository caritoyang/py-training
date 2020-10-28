num1=int(input("1st Num: "))
num2=int(input("2nd Num: "))
num3=int(input("3rd Num: "))

if(num1>num2 and num1>num3):
    print("The largest number is: " + str(num1))
elif(num2>num3 and num2>num1):
    print("The largest number is: " + str(num2))
else:
    print("The largest number is: " + str(num3))


if(num1<num2 and num1<num3):
    print("The lowest number is: " + str(num1))
elif(num2<num3 and num2<num1):
    print("The lowest number is: " + str(num2))
else:
    print("The largest number is: " + str(num3))