#Function: Validate Float values ​​for inputs.
def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print('Invalid input. Please enter a valid number.')

#Function: Validate Int values ​​for inputs.
def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Invalid input. Please enter a valid number.')