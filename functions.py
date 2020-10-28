# Create functions

def testing():
    "First line of the function is optional, and it can be used for commenting, it doesnt need #"
    print("This is KinuSolutions.")
    return # End of the function

def sum(a,b):
    c=a+b
    print("The sum of these both number is: " + str(c))

sum(10,5)

#####################################
# Taking argument and return value  #
#####################################
def multiply(a,b):
    c=a*b
    return c
def addition(a,b):
    c=a+b
    print("\n Final result: " + str(c))

x = multiply(4,20)
addition(x,10)

#####################################
#  No argument but return a value   #
#####################################
def retData():
    a=100
    return a
x = retData()
print(x)