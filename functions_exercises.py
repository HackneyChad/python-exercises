# 4.4_function_exercises.py  renamed to function_exercises for the import exercise
# Hackney,_Chad
# 5_Mar_19

#================================== COMPLETED =================================#
print('If you see this message, the file is working properly.')

#================================== COMPLETED =================================#
# Exercises
# Create a file named 4.4_function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1 =============================== COMPLETED =================================#
# Define a function named is_two. # It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.

def is_two(number):
    if number in ['2', '2.0', 'two', 2, 2.0]:
        return True
    else:
        return False

print(is_two('2'))


# # below is preferred syntax:
# def is_two(input):
#     return input == '2' or input == '2.0' or input ==  'two' or input == 2 or input == 2.0

# print(is_two(2))

# 2 =============================== COMPLETED =================================#
# Define a function named is_vowel.
# It should return True if the passed string is a vowel, False otherwise.

# def is_vowel(input):
#     if input in 'aeiou':
#         return True
#     else:
#         return False

# is_vowel('u')

# or, this version below is preferred syntax...
def is_vowel(input):
    return input in 'aeiou'

print(is_vowel('a'))


# 3 =============================== COMPLETED =================================#
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(input):
    if input not in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

print(is_consonant('z'))

# # or, this version below is preferred syntax...
# def is_consonant(input):
#     return input not in 'aeiou'

# print(is_consonant('a'))
# print(is_consonant('e'))
# print(is_consonant('y'))
# print(is_consonant('z'))
# print(is_consonant('b'))


# 4 =============================== COMPLETED =================================#
# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word
# if the word starts with a consonant.

# def is_word(word):
#     if word[:1] not in  ['a', 'e', 'i', 'o', 'u']:
#         print(word.title())
#     else:
#         print(word)

# is_word('monkey')


# # zachs code example:
# def cap_if_consonant(word):
#     first_letter = word[0]
#     if is_consonant(first_letter):
#         return word[0].upper() + word[1:].lower()
#     else:
#         return word

# # clever solution:
# # def cap_if_consonant(word):
# #     first_letter, *rest_of_letters = word
# #     return first_letter.upper() + rest_of_letters.lower() if is_consonant(first_letter) else word

# cap_if_consonant('codeup')
# cap_if_consonant('ada')
# cap_if_consonant('Codeup')
# cap_if_consonant('Ada')



# 5 =============================== COMPLETED =================================#
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# My code
# def calculate_tip(percentage, bill_total):
#     return bill_total * percentage

# print(calculate_tip(0.2, 20))
# print(calculate_tip(0.15, 10))

# previously, I had subbed in the info below between "return bill_total..." and the end of function
# # percentage = .15
# # bill_total = 25
# # arguments = [.15, 25]
# # tip = calculate_tip(*arguments)

# # print(f'Tip amount: ${tip:,}')
# # # this logic in/around the {} adds the dollar sign and comma separator, if needed.


# # Alternate solution:
# def calculate_tip(percentage, bill_total):
#     return bill_total * percentage
# print('Tip amount:')
# print(calculate_tip(percentage = .15, bill_total = 25))

# 6 =============================== COMPLETED =================================#
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# # my code
# def apply_discount(original, disc_percentage):
#     return (original - (original * disc_percentage))

# original = 25
# disc_percentage = 0.05
# arguments = [25, 0.05]
# calculator = apply_discount(*arguments)

# print(f'Price after discount applied: ${calculator:,}')


# # zach code
# def apply_discount(price, discount_percent):
#     discount_amount = price * discount_percent
#     return price - discount_amount

# apply_discount(50, .8)
# apply_discount(10, .2)


# 7 =============================== NEEDS HELP =================================#
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# # zachs code
# def handle_commas(a_string):
#     string_without_commas = a_string.replace(',', '')
#     return int(string_without_commas)

# handle_commas('1,234') # 1234
# handle_commas('123,456,789') # 1234


# # mine, in progress
# # def handle_commas(input):
# #     if ',' in input:
# #         return input

# # input = 2,000
# # print(handle_commas(input))


# # def handle_commas(input):
# #     if input > 2:
# #         return input

# # input = 5
# # print(handle_commas(input))


# 8 =============================== COMPLETED =================================#
# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).

# # my code:
# def get_letter_grade(numerical_grade):
#     if numerical_grade >= 88:
#         return('A')
#     elif numerical_grade >= 80 and numerical_grade <= 87:
#         return('B')
#     elif numerical_grade >= 67 and numerical_grade <= 79:
#         return('C')
#     elif numerical_grade >= 60 and numerical_grade <= 66:
#         return('D')
#     else:
#         return('F')

# print('The associated letter grade is: ')
# print(get_letter_grade(78))
# print()


# zach code:
# def get_letter_grade(numerical_grade):
#     if numerical_grade >= 88:
#         return 'A'
#     elif numerical_grade >= 80 and numerical_grade <= 87:
#         return 'B'
#     elif numerical_grade >= 67 and numerical_grade <= 79:
#         return 'C'
#     elif numerical_grade >= 60 and numerical_grade <= 66:
#         return 'D'
#     else:
#         return 'F'

# get_letter_grade(78)
# get_letter_grade(50)
# get_letter_grade(99)
# get_letter_grade(88)


# 9 =============================== COMPLETED ==================================#
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# ZACH ALSO HAS SOME CLEVER SOLUTIONS TO THIS ON THE GITHUB

# vowels = 'aeiouAEIOU'
# def remove_vowels(a_string):
#     for vowel in vowels:
#         a_string = a_string.replace(vowel,'')
#     return a_string
    
# print(remove_vowels('monkey'))

# 10 ============================== START HERE =================================#
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# x anything that is not a valid python identifier should be removed
# x leading and trailing whitespace should be removed
# x everything should be lowercase
# x spaces should be replaced with underscores
# cannot start with a digit
# cannot be a python key word
# no special characters

# for example:
# x Name will become name
# x First Name will become first_name
# x % Completed will become completed


# all caps variable name means this variable is a constant, this variable cannot change while the script is running.
# constant variables should only be listed outside the function below.
# LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789'

# def normalize_name(a_string):
#     a_string = a_string.lower()
#     valid_characters = []
#     for character in a_string:
#         if character in LETTERS:
#             valid_characters.append(character)
#     return ''.join(valid_characters).strip().replace(' ', '_')

# # this bottom 'print' piece here works well... reuse it if needed.
# print("normalize_name('Name') == {}".format(normalize_name('Name')))
# print("normalize_name('First Name') == {}".format(normalize_name('First Name')))
# print("normalize_name('Percent completed') == {}".format(normalize_name('Percent completed')))


# mine below
# def normalize_name(input):
#     if len(input) > 100:
#         print('Please stay below 100 characters. Please try again. ')
#     if input[:1].isdigit():
#         print('Please start name with a letter, not number. Please try again. ')
#     if     mystring.replace(' ', '_')
#     else:
#         return input #.lower()
 
#     # replace underscores
#     # input.strip()
#     # input.strip() re special characters !, @, #, $, % remove non ascii letters

#     # test using one leading number, add leading-trailing spaces,
# # special characters, keywords, uppers


# 11 ============================== START HERE =================================#
# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# # cumulative sum [1,1,1]
# # means...
# # [
# # first item, 1
# # second item is first item plus the next item in the list, 2
# # third item is the previous number (2) plus the next number (1), 3
# # ]

# # zach example:
# def cumsum(numbers):
#     sums = [numbers[0]]
#     for current_number in numbers[1:]:
#         last_number = sums[-1]
#         next_number = last_number + current_number
#         sums.append(next_number)

#     return sums 

# print("cumsum([1, 1, 1]) == %s" % cumsum([1, 1, 1]))
# print("cumsum([1, 2, 3]) == %s" % cumsum([1, 2, 3]))
# print("cumsum([1, 2, 3, 4]) == %s" % cumsum([1, 2, 3, 4]))
# print("cumsum([1, -2, 1]) == %s" % cumsum([1, -2, 1]))


# BONUS =========================== START HERE =================================#
# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# BONUS =========================== START HERE =================================#
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27


#=================================== END HERE ==================================#