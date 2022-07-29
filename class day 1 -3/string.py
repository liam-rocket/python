
import math

# from __future__ import division
print("What should we eat for {}".format("DINNER"))


res = 100.00/777.00
print(res)


def convertKmToMiles(distanceInKm):
    return distanceInKm * 2.2

print(convertKmToMiles(20))



def test(input):
    random_dice_number = 10

    if random_dice_number == input or random_dice_number + 1 == input or random_dice_number - 1 == input:
        return 'hi'

number = input('enter a number=')

# x = float(number)

is_nan = math.isnan(number)

print(is_nan)