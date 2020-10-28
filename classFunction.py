class A:

    # Function with no argument and no return value
    def hello(self):
        print("Hello World")

    # Function with 2 arguments and no return value
    def sum(self,a,b):
        c=a+b
        print("Sum is: " + str(c))

    # Function with argument and return value
    def mul(self,a,b):
        c=a*b
        return c

obj=A()
# obj.hello()
# obj.sum(30,70)
#
# x=obj.mul(2,5)
# print(x)