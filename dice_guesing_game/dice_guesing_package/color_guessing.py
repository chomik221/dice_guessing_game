# modul for tiping colors

# import random modul 

import random as rn 

# generate color  

colors_list = ['Green', 'Red', 'Blue', 'Yellow', 'Orange', 'Pink', 'Black', 'White']

def generate_color():
    color_index = rn.randrange(0, len(colors_list))
    generated_color = colors_list[color_index]
    return generated_color

# guess color

def guess_color():
    while True:
        try:
            user_guess = int(input("Guess color. Green: '0', Red: '1', Blue: '2', Yellow: '3', Orange: '4', Pink: '5', Black: '6', White: '7'"))
            guesed_color = colors_list[user_guess]
            return guesed_color
        except ValueError:
            print("Invalid Input! Please enter number in given range")

# evaluate guess 

def evaluate_color_guess(user_guess, generated_color):
    if user_guess == generated_color:
        return True
    else:
        return False
