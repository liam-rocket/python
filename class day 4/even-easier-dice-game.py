import random

def roll_dice():
    my_random_value = random.randint(1, 6)
    return my_random_value

def main(guess):
    if guess != 'even' and guess != 'odd':
        return 'input can only be even or odd'

    dice_roll = roll_dice()

    output = 'you lose'

    print("dice_roll =", dice_roll)
    if guess == 'even':
        if (dice_roll % 2) == 0:
            output = 'you win'
    else:
        if (dice_roll % 2) != 0:
            output = 'you win'
    
    return output

user_guess = input('odd or even=')
result = main(user_guess)

print(result)
