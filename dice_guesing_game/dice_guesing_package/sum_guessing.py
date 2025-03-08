# modul for typing numbers

# import random module

import random as rn 

# sum guess

def generate_throw_count():
    throw_count = rn.randrange(2,12)
    return throw_count

# guess type 

def guess_throw():
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            return user_guess
        except ValueError:
            print("Invalid Input! Please enter number")

# evaluate guess

def evaluate_guess (guess, throw_count):
    if guess == throw_count:
        return True
    else:
        return False
