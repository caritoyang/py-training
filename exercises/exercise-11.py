# Fibonacci
num=int(input("Insert a Number: "))
start=0
last=1
new=0

for i in range(num):
    if(new>num):
        break
    print(start)
    new=start+last
    last=start
    start=new
