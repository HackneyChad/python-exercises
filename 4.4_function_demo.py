# 4.4_function_demo.py
# Hackney,_Chad
# 06 Mar 19

# How to approach a problem
## Problem:  get odd number from user in range (1-50)
    # break problem into pieces:
    # first, get an integer from user;
    # second, determine if that integer is odd;
    # third, determine if that integer is within the assigned (1-50) range.

#VERIFY THIS CODE FROM ZACHs CODE ON GITHUB:


#==================================== COMPLETED ====================================#
# determines if a number is even or odd.
def is_even(n):
    return n % 2 == 0

# gets initial input from user.
def get_integer_input(prompt):
    user_input = input(prompt)
    if not user_input.isdigit():
        print('Error: {} is not an integer'.format(user_input))
        print()
        return get_integer_input(prompt)
        # this checks if number entered is a digit, and if not, prompt user again.
    return int(user_input)

# determines if user-provided number is odd, see first function above.
def get_odd_number_input(prompt):
    user_input = get_integer_input(prompt)
    print()
    if is_even(user_input):
        print('Error: {} is an even number'. format(user_input))
        return get_odd_number_input(prompt)
    return user_input

# determines if user-provided number is within range.
def get_odd_number_in_range(prompt, min, max):
    user_input = get_odd_number_input(prompt)
    if user_input < min or user_input > max:
        msg = ('Error: {} is not in the range ({}-{})')
        print(msg.format(user_input, min, max))
        return get_odd_number_in_range(prompt, min, max)
    return user_input

print('<<< Program Start! >>>')
print()

prompt = 'Please enter an odd integer: (1-50) '
print()
inputted_number = get_odd_number_in_range(prompt, 1, 50)
print()

print()
print('user gave us: {}'.format(inputted_number))
print('user gave us a {}'.format(type(inputted_number)))
print()

#====================================== END ======================================#
