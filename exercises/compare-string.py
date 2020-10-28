def compare1(a,b):
    if(a[len(a)-10:len(a)].upper()==b[len(b)-10:len(b)].upper()):
        print("It's equal.")
    else:
        print("It's different.")

# compare1("This is KinuSolutions.","I don't know what else to put BUT KinuSolutions.")


def compare2(a,b):
    if(a[0:3].lower()==b[0:3].lower()):
        print("It's equal.")
    else:
        print("It's different.")

# compare2("Hello","Helman")


def compare3(text,b):
    count=0
    list=text.split(" ")
    for i in list:
            if(i.lower()==b.lower()):
                count+=1
    print("The word " + b + " appears " + str(count) + " times.")

# compare3("This is Kinu, this is KinuSolutions", "This")


def palend(a):
    if(a[::-1]==a):
        print("The word is palendrome.")
    else:
        print("NOT palendrome.")

# palend("malayalam")


def totalLen(a,b):
    c=a+b
    print(len(c))

# totalLen("Hello","KinuSolutions")


def words(text):
    list=text.split(" ")
    print(len(list))
    total=0
    totalM=0
    for i in list:
        total = 0
        for j in list:
            if(i.lower()==j.lower()):
                total+=1
            if(total>totalM):
                totalM=total
                repWord=j
    print('Most repeated word: ' + repWord.upper() + ' appears ' + str(totalM) + ' times. ')

# words("This is this and this is not that.")


def liToSt(text):
    list=text.split(" ")
    newText=""
    for i in list:
        newText=newText+i
    print(newText)

liToSt("Testing this new sentence to show without spaces.")