
# Set a function that converts ml to to litres
def convert_ML_to_L(ml):
    return ml / 1000

def calc_oranges_needed(number_of_guests):
    # assign the values to variables. Why? Assigning values to variables helps prevent errors when we have to re-use these numbers (e.g. when our apps become larger/more complex in future)
    oranges_per_glass = 4
    # calculate the oranges we'll need given the number of guests
    oranges_needed = number_of_guests * oranges_per_glass
    return oranges_needed

def calc_l_needed(number_of_guests):
    # asssign values to variables
    ml_per_glass = 90.0
    # convert mlPerGlass to Litres per glass. Notice tt we are executing an external fn within this fn in order to achieve this.
    litres_per_glass = ml_per_glass / 1000
    # calculate the vol (in litres) of  juice we'll need, given the number of guests.
    litres_needed = number_of_guests * litres_per_glass
    # return the litresNeeded. toFixed allows you to set the ans to # decimal places
    return round(litres_needed, 2)

def main(input):
    oranges_needed = calc_oranges_needed(input)
    vol_juice_needed = calc_l_needed(input)

    output = "We need ${} oranges to make ${}Ls of juice for ${} guests".format(oranges_needed, vol_juice_needed, input);
    return output

num_of_guest = input('num of guest=')

result = main(num_of_guest)

print(result)