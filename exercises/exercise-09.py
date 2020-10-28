number=int(11)
for i in range(1,10):
    if((number*i)%3==0 or (number*i)%5==0 or (number*i)%7==0):
        continue
    print(number*i)

#################################
#  Take input number from User

input_num = int(input("Please enter your number --- > "))
# Print table of given number but only display number where multiple is not divisible of 3, 5, 7
for i in range(1, 11):
    num = input_num * i

    if (num % 3 != 0 and num % 5 != 0 and num % 7 != 0):
        print(num)