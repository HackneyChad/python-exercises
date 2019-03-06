# 4.4_function_exercises.py
# Hackney,_Chad
# 5_Mar_19

#================================== COMPLETED =================================#
print()
print()
print('If you see this message, the file is working properly.')
print()

#================================== COMPLETED =================================#
# Exercises
# Create a file named 4.4_function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1 =============================== COMPLETED =================================#
# Define a function named is_two. # It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.

# def is_two(input):
#     if input in ['2', '2.0', 'two', 2, 2.0]:
#         return True
#     else:
#         return False

# print(is_two('2'))

# 2 =============================== COMPLETED =================================#
# Define a function named is_vowel.
# It should return True if the passed string is a vowel, False otherwise.

# def is_vowel(input):
#     if input in ['a', 'e', 'i', 'o', 'u']:
#         return True
#     else:
#         return False

# print(is_vowel('u'))

# 3 =============================== COMPLETED =================================#
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# def is_consonant(input):
#     if input not in ['a', 'e', 'i', 'o', 'u']:
#         return True
#     else:
#         return False

# print(is_consonant('z'))

# 4 =============================== COMPLETED =================================#
# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word
# if the word starts with a consonant.

# def is_word(input):
#     if input[:1] not in  ['a', 'e', 'i', 'o', 'u']:
#         print(input.title())
#     else:
#         print(input)

# is_word('monkey')

# 5 =============================== COMPLETED =================================#
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# def calculate_tip(percentage, bill_total):
#     return bill_total * percentage

# percentage = .15
# bill_total = 25
# arguments = [.15, 25]
# tip = calculate_tip(*arguments)

# print(f'Tip amount: ${tip:,}')
# # this logic in/around the {} adds the dollar sign and comma separator, if needed.


# # Alternate solution:
# def calculate_tip(percentage, bill_total):
#     return bill_total * percentage
# print('Tip amount:')
# print(calculate_tip(percentage = .15, bill_total = 25))

# 6 =============================== COMPLETED =================================#
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# def apply_discount(original, disc_percentage):
#     return (original - (original * disc_percentage))

# original = 25
# disc_percentage = 0.05
# arguments = [25, 0.05]
# calculator = apply_discount(*arguments)

# print(f'Price after discount applied: ${calculator:,}')

# 7 =============================== NEEDS HELP =================================#
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(input):
    if ',' in input:
        return input

input = 2,000
print(handle_commas(input))


def handle_commas(input):
    if input > 2:
        return input

input = 5
print(handle_commas(input))




# 8 =============================== COMPLETED =================================#
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# def get_letter_grade(input):
#     if input >= 88:
#         return('A')
#     elif input >= 80 and input <= 87:
#         return('B')
#     elif input >= 67 and input <= 79:
#         return('C')
#     elif input >= 60 and input <= 66:
#         return('D')
#     else:
#         return('F')

# print('The associated letter grade is: ')
# print(get_letter_grade(78))
# print()

# 9 =============================== COMPLETED ==================================#
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# def remove_vowels(input):
#     for i in 'aeiouAEIOU':
#         input = input.replace(i,'')
#     return input
    
# print(remove_vowels('pickle'))

# 10 ============================== START HERE =================================#
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed


# 11 ============================== START HERE =================================#
# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# BONUS =========================== START HERE =================================#
# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# BONUS =========================== START HERE =================================#
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27


#=================================== END HERE ==================================#
