# Required Arguments (a & b)

def takeInput(a,b):
    c=a+b
    print("Sum of values: " + str(c))

takeInput(20,30)

# Keyword Arguments (specify the value for each argument)
def takeMyInput(a,b):
    c = a + b
    print("Sum of values: " + str(c))

takeMyInput(b=500,a=100)


# Default Arguments
# (if you only pass one arg, the missing argument will use the default value
# the default value must be define always at the end)
def takeDefArg(a,b=10):
    c = a + b
    print("Sum of values: " + str(c))

takeDefArg(20)