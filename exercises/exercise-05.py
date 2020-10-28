side1=int(input("Side 1: "))
side2=int(input("Side 2: "))
side3=int(input("Side 3: "))

if(side1==side2 and side2==side3):
    print("EQUILATERAL.")
elif(side1==side2 or side2==side3 or side3==side1):
    print("ISOSCELES.")
else:
    print("SCALENE.")