def main(input):
    my_output_value = 'Hello World'

    if input == 'Liam is a good teacher':
        my_output_value = 'You wrote the secret phrase !'

    return my_output_value


result = main('Liam is a good teacher')

print(result)