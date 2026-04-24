# Guessing game
from random import randint

def guess():
    answer = randint(1,10)

    while True:
        try:
            make_guess = int(input('To play 🎮🎮\n Guess a number between 1-10:  '))
        except ValueError:
            print( 'That is not a number! 🤷')
            continue

        if make_guess == answer:
            print(f"Cheers!! 🥂 \n You guessed the right number: {answer} 👏")
            break
        else:
            print (f"You guessed wrongly! ❌ \nTry again 💪🏻")
            
guess()
