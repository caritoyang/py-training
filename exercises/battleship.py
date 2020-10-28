import string
import random

def split(word):
    return list(word)

rows=int(input("Number of rows: "))
columns=int(input("Number of columns: "))
board={}

abc=string.ascii_uppercase
list=split(abc)

for i in range(0,rows):
    board[list[i]] = []
    for j in range(0,columns):
        board[list[i]].append(0)

def createBoat(boat, direction):
    col=random.randint(1, columns-boat)
    row=random.randint(1, rows-boat)
    boatcheck = 1
    while (boatcheck == 1)
        col = random.randint(1, columns - boat)
        row = random.randint(1, rows - boat)
    boatcheck = board[list[row]][col]
    for i in range(0,boat):
        board[list[row]][col]=1
        if(direction):
            col+=1
        else:
            row+=1


boats=[2,2,3,4,4,5]
for i in boats:
    direction=random.randint(0,1)
    createBoat(i,direction)


for row in board:
    print(board[row])
