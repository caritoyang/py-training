maths=int(input("Math: "))
english=int(input("English: "))
physics=int(input("Physics: "))
chemestry=int(input("Chemestry: "))
biology=int(input("Biology: "))

average=(maths+english+physics+chemestry+biology)/5

if(average>90):
    print("GRADE A.")
elif(average>80):
    print("GRADE B.")
elif (average > 70):
    print("GRADE C.")
elif(average>60):
    print("GRADE D.")
elif(average>50):
    print("GRADE E.")
else:
    print("GRADE F.")
