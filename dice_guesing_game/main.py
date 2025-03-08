# Import dice guessing package
from dice_guesing_package import generate_throw_count, guess_throw, evaluate_guess, generate_color, guess_color, evaluate_color_guess 

# Choose game
def choose_game():
    while True:
        user_choice = input("Choose game. Dice guess: 'D', Color guess: 'C': ").lower()
        if user_choice in ('d', 'c'):
            return user_choice
        else:
            print("Invalid input! Please choose from given values")

# dice game

def dice_game(evaluation, user_guess, throw_count):
    if evaluation:
        print(f"Your guess {user_guess} was right!")
    else:
        print(f"Your guess {user_guess} wasn't right. The throw count is {throw_count}")

# Color game

def color_game(evaluation, user_guess, color):
    if evaluation:
        print(f"Your guess {user_guess} was right!")
    else:
        print(f"Your guess {user_guess} wasn't right. The color is {color}") 

# play game 

def play_game(chosen_game):
    if chosen_game == 'd':
        throw_count = generate_throw_count()
        throw_guess = guess_throw()
        evaluation = evaluate_guess(throw_guess, throw_count)
        dice_game(evaluation, throw_guess, throw_count)
    elif chosen_game == 'c':
        color = generate_color()
        color_guess_result = guess_color()
        evaluation = evaluate_color_guess(color_guess_result, color)
        color_game(evaluation, color_guess_result, color)

# game cycle

while True:
    chosen_game = choose_game()
    play_game(chosen_game)
    play_again = input("Do you want to play again? (Y/N): ").lower()

    if play_again != 'y':
        print("GAME OVER")
        break
