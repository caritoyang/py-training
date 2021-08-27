import string
import random

def split(word):
    return list(word)

rows=int(input("Number of rows: "))
columns=int(input("Number of columns: "))
colList=[]
board={}
boardPlayer={}
boardR = []
boardRL = []
h = 0

for i in range(0,columns+1):
    colList.insert(i,i)

abc=string.ascii_uppercase
list=split(abc)

for i in range(0,rows):
    board[list[i]] = []
    boardR.insert(i,list[i])
    if i%2==0:
        boardRL.insert(h, list[i])
        h=h+1
    for j in range(0,columns):
        board[list[i]].append(0)

for i in range(0,rows):
    boardPlayer[list[i]] = []
    for j in range(0,columns):
        boardPlayer[list[i]].append(0)


def checkBoardForBoat(boat, direction, row, col):
    for i in range(0, boat):
        if board[list[row]][col]>0:
            return True
        if direction:
            col=col+1
        else:
            row=row+1
    return False


def createBoat(boat, direction):
    col = random.randint(1, columns - boat)
    row = random.randint(1, rows - boat)
    boardSpaceTaken = True
    while boardSpaceTaken == True:
        col = random.randint(1, columns - boat)
        row = random.randint(1, rows - boat)
        boardSpaceTaken = checkBoardForBoat(boat,direction,row,col)
    for i in range(0,boat):
        board[list[row]][col]=1
        if(direction):
            col=col+1
        else:
            row=row+1

boats=[2,3,3,4]

for i in boats:
    direction=random.randint(0,1)
    createBoat(i,direction)


# for row in board:
#     print(board[row])

def printPlayerBoard():
    for j in boardR:
        if j == list[0]:
            for i in range(0, columns+1):
                if i == columns:
                        print('\x1b[2;30;47m' + str(colList[i]).ljust(3,' ') + '\x1b[0m')
                elif i > 9:
                    print('\x1b[2;30;47m' + str(colList[i]).ljust(3,' ') + '\x1b[0m', end="")
                else:
                    print('\x1b[2;30;47m' + str(colList[i]).ljust(3,' ') + '\x1b[0m', end="")
        for i in range(0, columns):
            if i == columns-1:
                print(" " + str(boardPlayer[j][i]) + " ")
            elif i == 0:
                print('\x1b[2;30;47m' + j + " " + '\x1b[0m', end="")
                print(" " + str(boardPlayer[j][i]), end=" ")
            else:
                print(" " + str(boardPlayer[j][i]), end=" ")


hit = 0
tries = 0
totalH = sum(boats)

while hit < totalH:
    print('=========================================')
    print('There are 4 boats: ' + str(boats))
    print('Played ' + str(tries) + ' times.\n')
    rowP = 'Z'
    colP = 50
    while rowP not in boardR:
        rowP = str(input("Select row(A-J): ").upper())
    while colP < 1 or colP > columns-1:
        try:
            colP = int(input("Select column(1-" + str(columns) + "): "))
        except ValueError:
            print("Please input a number from 1 to " + str(columns))
    if boardPlayer[rowP][colP-1] == '\x1b[0;31;41m' + 'H' + '\x1b[0m' or boardPlayer[rowP][colP-1] == '\x1b[2;34;44m' + 'W' + '\x1b[0m' or boardPlayer[rowP][colP-1] == '\x1b[0;36;46m' + 'W' + '\x1b[0m':
        print('This slot has been played already.\n')
    else:
        if board[rowP][colP-1] == 1:
            hit = hit+1
            boardPlayer[rowP][colP-1] = '\x1b[0;31;41m' + 'H' + '\x1b[0m'
            printPlayerBoard()
            print("\nHIT!\n")
            tries = tries + 1

        else:
            if rowP in boardRL:
                boardPlayer[rowP][colP-1] = '\x1b[0;36;46m' + 'W' + '\x1b[0m'
            else:
                boardPlayer[rowP][colP - 1] = '\x1b[2;34;44m' + 'W' + '\x1b[0m'
            printPlayerBoard()
            print("\nYou missed!\n")
            tries = tries + 1

print('YOU WON after ' + str(tries) + " tries.")