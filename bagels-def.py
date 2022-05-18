from random import randint
from tabnanny import check
guess = str(randint(0,1000))

print("""
Bagels, a deductive logic game.
I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

I have thought up a number.
You have 10 guesses to get it.

 """)

def check_number(num, guess, position, pin1, pin2):
    if num in guess:
        if num in guess[position]:
            print("Fermi", end=" ")
        else:
            if num !=pin1 or num!=pin2:
                print("Pico", end=" ")

def play(guess):
    for i in range(1, 11):
        user_input = input(f'\nGuess # {i}\n')
        while (int(user_input)<100) or (int(user_input)>999):
            user_input = input(f'Please insert a number between 100-999\n')
        fir = user_input[0]
        sec = user_input[1]
        thi = user_input[2]
        
        if user_input == guess:
            print("You got it!")
            question()
            break
        else:
            check_number(fir, guess, 0, sec, thi)
            check_number(sec, guess, 1, fir, thi)
            check_number(thi, guess, 2, fir, sec)
            if fir not in guess and sec not in guess and thi not in guess:
                print("Bagels", end=" ")
    print("\nYou've Lost!")
    question()

def question():    
    answer = input("\nDo you want to play again? (yes/no)\n")
    if answer.upper() == "YES":
        guess = str(randint(0,1000))
        play(guess)
    else:
        print("Thank you for playing, see you next time!")

play(guess)
