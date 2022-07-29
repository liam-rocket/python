import random

def roll_dice():
    my_random_value = random.randint(1, 6)
    return my_random_value

def main(guess):
    dice_roll = roll_dice()

    output = 'you lose'

    

    return output

user_guess = input('your guess=')
result = main(user_guess)

print(result)
