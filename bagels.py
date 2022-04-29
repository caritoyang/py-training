from random import randint
guess = str(randint(0,1000))

print("""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
 """)

for i in range(1, 11):
    user_input = input(f'\nGuess # {i}\n')
    while (int(user_input)<100) or (int(user_input)>999):
        user_input = input(f'Please insert a number between 100-999\n')
    fir = user_input[0]
    sec = user_input[1]
    thi = user_input[2]
    
    if user_input == guess:
        print("You got it!")
        break
    else:
        if fir in guess:
            if fir in guess[0]:
                print("Fermi", end=" ")
            else:
                print("Pico", end=" ")
        if sec in guess:
            if sec in guess[1]:
                print("Fermi", end=" ")
            else:
                print("Pico", end=" ")
        if thi in guess:
            if thi in guess[2]:
                print("Fermi", end=" ")
            else:
                print("Pico", end=" ")
        if fir not in guess and sec not in guess and thi not in guess:
            print("Bagels", end=" ")
