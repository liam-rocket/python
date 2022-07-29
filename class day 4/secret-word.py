# Declare a function
def main(password):
    door = 'closed'

    # An example of an "if condition" that checks whether input equals 'Liam is a good teacher'
    if password == 'Liam is a good teacher' or password == '...' or password == '...' :
        # my_output_value is only changed to the below if the above "if condition" is met
        door = 'open'

    return door

# assigning our output value into a variable called "result"
result = main('Liam is a good teacher')

print(result)