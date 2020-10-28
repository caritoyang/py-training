month=int(input("Select a Month: "))

if(month<13):
    if(month==2):
        print("This month has 28 days.")
    elif(month<8 and month%2==0):
        print("This month has 30 days.")
    elif(month>7 and month%2==0):
        print("This month has 31 days.")
    elif(month>8 and month%2!= 0):
        print("This month has 30 days.")
    else:
        print("This month has 31 days.")
else:
    print("INCORRECT MONTH")