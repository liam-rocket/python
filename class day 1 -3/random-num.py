import random

def roll_dice():
    my_random_value = random.randint(1, 6)
    return my_random_value

def dice_game(input):
    random_dice_number = roll_dice()

    output_value = 'your lose'

    if int(input) == random_dice_number or int(input) + 1 == random_dice_number:
        output_value = 'you win'

    print(random_dice_number)
    return output_value

result = dice_game(3)
print(result)