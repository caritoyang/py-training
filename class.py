# Creating a class
class A:
    # Constructors are automatically called when object is created
    # Can take Arguments
    # Never return any value
    # Used for initialization
    def __init__(self,a,b):
        c=a+b
        print("This is Constructor. It can take arguments. " + str(c))

    # Class function
    def welcome(self):
        print("This is Class function.")

# To call any member of class, create OBJECT of the class
obj=A(20,30)

# Call functions of class by using object
obj.welcome()