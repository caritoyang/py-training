name=input("Name: ")
math=int(input("Math: "))
science=int(input("Science: "))
english=int(input("English: "))

percentage=(math+science+english)/3

print("User name is " + name + ", Scored " + str(percentage) + "% in exams.")