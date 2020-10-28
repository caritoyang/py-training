# Exception handling - try except finally

try:
    user_input1 = input("Please enter first number: ")
    user_input2 = int(input("Please enter second number: "))
    c = user_input1 + user_input2
    print(c)
except:
    print("Your input is incorrect, please enter correct data.")
    print(user_input1 + " is not a number.")
finally:
    print("This code I want to execute always at the end.")