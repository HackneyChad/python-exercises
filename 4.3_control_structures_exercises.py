# 4.3_control_structures.py
# Hackney, Chad
# 04 Mar 19

# file test
print()
#print('File is working properly')
print()


# Exercises
# Do your work for this exercise in a file named 4.3_control_structures_exercises.py.


print()

## ================================================================================ ##
# 1. Conditional Basics


# COMPLETED
# prompt the user for a day of the week, print out whether the day is Monday or not.

# # CODE:
# weekday = input('Please enter a weekday: ')
# print(f'weekday = {weekday}')
# if weekday == 'Monday':
#     print('Sounds like someone has a case of the Mondays!')
# else:
#     print('It is NOT Monday.')


## ================================================================================ ##

# COMPLETED
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# CODE:
# weekday = input('Please enter a day of the week: ')
# if weekday.lower().startswith('s'):
# # or... if weekday = 'Saturday' or weekday = 'saturday' or weekday = 'Sunday' or weekday = 'sunday':
#     print('Hooray, it is the weekend!')
# else:
#     print('Sorry, it is a weekday.')
# print()

# CODE:
# OR... alternatively...
# weekend_days = ['saturday', 'sunday', 'sat', 'sun']
# weekend = input('Enter a weekday: ')
# if weekend.lower() in weekend_days:
#     print('It is the weekend.')
# else:
#     print('Sorry, weekday...')


## ================================================================================ ##

# COMPLETED
# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be

# write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours

# CODE:
# hours_worked = 43
# hourly_rate = 100
# if hours_worked > 40:
#     paycheck_at_reg_rate = hourly_rate * 40
#     overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
#     paycheck = paycheck_at_reg_rate + overtime_pay
# else:
#     paycheck = hours_worked * hourly_rate
# print('Paycheck amount is:')
# print()
# print(paycheck)
# print()
# print()


## ================================================================================ ##

# 2. Loop Basics
# While

# COMPLETED
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

# Your output should look like this:
# 5 6 7 8 9 10 11 12 13 14 15

# # CODE:
# i = int(5)
# while i <= 15:
#     print(i)
#     i += 1


# COMPLETED
# Create a while loop that will count by 2's starting with 0 and ending at 100.
# Follow each number with a new line.

# # CODE:
# for i in range(0, 100):
#     # skip numbers evenly divisible by 2, ie 'even numbers'.
#     is_divisible_by_two = i % 2 == 0
#     if is_divisible_by_two:
#         continue
#     print(i)


# # OR, alternatively:
# i = 0               # starting point of loop: 'starting with 0...'
# while i <= 100:     # upper max of loop: '...and ending at 100'
#     print(i)
#     i += 2          # loop counts incrementally by 2


# COMPLETED
# Alter your loop to count backwards by 5's from 100 to -10.
# CODE:
# i = (100)        # starting point of loop: 'from 100...'
# while i >= -10:  # min lower limit of loop '...to -10'
#     print(i)
#     i -= 5       # displays loop numbers decrementing by 5 each iteration


# COMPLETED:
# Create a while loop that starts at 2, and displays the number squared on each line, while the number is less than 1,000,000.
# Output should equal:
# 2 4 16 256 65536

# CODE:
i = 2                 # starting point of loop
# while i < 1_000_000:    # max limit 'less than 1,000,000'
#     print(i)
#     i = i ** 2           # displays incremental squares of each i number
# could also finish with i *= i
# print()
# print('All Done')
# print()


# COMPLETED
# Write a loop that uses print to create the output shown below.
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

# # CODE:
# i = (100)       # starting point of loop: 'from 100 down to...'
# while i >= 5:   # ending point of loop: '...down to 0'
#     print(i)
#     i -= 5      # loop decrementally counts down by 5 each iteration.
# print()
# print('All Done')
# print()
#  see Zach's notes on an alternate way to do this using (start point, end point, increment or indecrment number)

## ================================================================================ ##

# For Loops

# COMPLETED
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# # CODE:
# num = int(input('Please enter a number: '))  # To take input from the user
# for i in range(1, 11):  # use of loop to iterate 10 times
#    print(num,'x',i,'=',num*i)  # writes '3 * 1 = 3', iterating through the range numbers.
# print()

# #Loops:  1. doit it once, 2. do it twice, 3. do it in a loop

# # test this out
# # n = 3
# x = int(input('Please enter a number: '))
# x = 7
# for n in range(1, 11):
#     output = '{} x {} = {}'.format(x, n, x * n)
#     print(output)


## ================================================================================ ##


# THIS STILL NEEDS SOME HELP
# Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# # CODE:   this does not quite generate the same results... see below.

# for i in range(1, 10):  # loop uses range numbers to iterate 10 times.
#    print(f'{i}' * i)       # loops through each number in the range, multiplying the number of instances of that number by that same number in the range, ie #3 appears 3 times, etc.
#    i += 1


# ########  GOOD INFO IMMEDIATELY BELOW:    #######
# # running this in pieces first
# print('1' * 1)
# print('2' * 2)
# print('3' * 3)
# # this works manually

# # then run it manually using n variable, changing the number each time:
# n = 3
# print(str(n) * n)
# # this works, so now automate it in a for loop below

# for n in range(1,10):
#     print(str(n) * n)


## ================================================================================ ##

# break and continue

# START HERE
# REMAINING TO DO

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input.

# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.



####    SEE ZACHS CODE ON THIS ON GITHUB    ####
# 2 parts to this problem:
# break the problem down into chunks to tackle individiaully

# 1. get *valid* number from user
# 2. do logic with that number acquired


# 1. get *valid* number from user
# while we have something that is not valid,
# keep prompting user for input

# 1
# number_to_skip = input('Gimme an odd number, (1-50): ')
# while not number_to_skip.isdigit() or int(number_to_skip) < 1 or int(number_to_skip) > 50 or int(number_to_skip) % 2 == 0:
#     number_to_skip = input('Gimme an odd number, (1-50): ')

# number_to_skip = int(number_to_skip)


# # 2. do logic with that number acquired:
# # for every number between 1 and 50
# # if number is even,
# # skip it,
# # if the number is the one that was entered,
# # print the special message
# # else:
# # print the number
# for n in range(1, 21):
#     if n % 2 == 0:
#         continue
#     if n == number_to_skip:
#         print(f'Yikes! Skipping number {n}')
#     else:
#         print(f'Here is an odd number {n}')


# # keep prompting for user input
# # if we have a valid imput, stop the loop
# while True:
#     number_to_skip = input('Gimme an odd number, (1-50): ')
#     if number_to_skip.isdigit() and int(number_to_skip) in range (1, 51) and int(number_to_skip) % 2 == 1:
#         break
       
#######  LOOK AT ZACHS CODE ON THIS... ON GITHUB....######


        # Your output should look like this:
        # Number to skip is: 27

        # Here is an odd number: 1
        # Here is an odd number: 3
        # Here is an odd number: 5
        # Here is an odd number: 7
        # Here is an odd number: 9
        # Here is an odd number: 11
        # Here is an odd number: 13
        # Here is an odd number: 15
        # Here is an odd number: 17
        # Here is an odd number: 19
        # Here is an odd number: 21
        # Here is an odd number: 23
        # Here is an odd number: 25
        # Yikes! Skipping number: 27
        # Here is an odd number: 29
        # Here is an odd number: 31
        # Here is an odd number: 33
        # Here is an odd number: 35
        # Here is an odd number: 37
        # Here is an odd number: 39
        # Here is an odd number: 41
        # Here is an odd number: 43
        # Here is an odd number: 45
        # Here is an odd number: 47
        # Here is an odd number: 49


# for n in range(10):
#     if n % 2 == 0:
#         continue
#     print('Here is an odd number: {}'.format(n))


## ================================================================================ ##

# 2.d.  -  COMPLETE
    # The input function can be used to prompt for input and use that input in your python code.
    # Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
    # (Hints: first make sure that the value the user entered is a valid number,
    # also note that the input function returns a string, so you'll need to convert this to a numeric type.)


# # CODE:
# user_input = input('Please enter a positive number: ')
# # until user enters something that looks like a number,
# # keep prompting for input
# while not user_input.isdigit():
#     user_input = input('Hey! Give me a number!')
# user_input = int(user_input)
# for n in range(0, user_input):
#      print(n)
# print('# iterates until the condition in the "for n" statement is satisfied.')

# CODE:
# print()
# # break loop example:
# print('break loop example:')
# for i in range(10):
#     print(i)
#     if i >= 8:
#         break
# print('# stops iterating when the "if" statement condition is satisfied.')

# # CODE:
# print()
# # continue loop example:
# print('continue loop example:')
# for i in range(1, 16):
#     # skip numbers evenly divisible by 3
#     is_divisible_by_three = i % 3 == 0
#     if is_divisible_by_three:
#         continue
#     print(i)
# print('# skips every number divisible by 3.')
# print()

## ================================================================================ ##

# COMPLETED

# 2.e. Write a program that prompts the user for a positive integer.
    # Next write a loop that prints out the numbers from the number the user entered down to 1.

# # CODE:
# user_input = input('Please enter a positive number: ')
# # until user enters something that looks like a number,
# # keep prompting for input
# while not user_input.isdigit():
#     user_input = input('Hey! Give me a number!')
# user_input = int(user_input)
# i = user_input
# while i >= 1:
#      print(i)
#      i -= 1
# print('# iterates until the condition in the "for n" statement is satisfied.')


## ================================================================================ ##

# COMPLETED

# 3.  Fizzbuzz
    # One of the most common interview questions for entry-level programmers is the FizzBuzz test.
    # Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
        # Write a program that prints the numbers from 1 to 100.
        # For multiples of three print "Fizz" instead of the number
        # For the multiples of five print "Buzz".
        # For numbers which are multiples of both three and five print "FizzBuzz".



######  ZACH HAS COOL LOGIC ON THIS, SEE CODE ON GITHUB   #######

# # CODE:
# for n in range(1, 100):
#     if n % 3 == 0 and n % 5 == 0:
## this line can also be written as 'if n%15 == 0' instead
#         print('FizzBuzz')
#     if n % 3 == 0:
#         print('Fizz')
#     if n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)
# print()
# print('All Done')
# print()

## ================================================================================ ##


# REMAINING TO DO

# 4. Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output
# What number would you like to go up to? 5
# Here is your table!
# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

# Bonus: Research python's format string specifiers to align the table


##### SEE ZACH CODE  ######
# upper_bound = int(input('Enter a number: '))
# # testing with static 'n' values first...  it's works.
# # n = 3
# # print('{} | {} | {}'.format(n, n ** 2, n** 3))
# # This sets up the headers
# print('number | squared | cubed')
# print('------ | ------- | -----')
# # now using the "for loop in range"
# for n in range(1, upper_bound + 1):
#     print('{} | {} | {}'.format(n, n ** 2, n** 3))

###  ZACH CODE ALSO SHOWS HOW TO FORMAT FOR ALIGNMENT, LEFT, RIGHT, ETC  ###
###  VERY IMPORTANT... RESEARCH THIS!!   ###



## ================================================================================ ##

# COMPLETED


# 5. Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# # CODE:
# grade = int(input('Please enter a numerical grade from 0 to 100: '))
# # for grade in range(1, 100):
# if grade >= 88:
#     print('A')
# elif grade >= 80 and grade <= 87:
#     print('B')
# elif grade >= 67 and grade <= 79:
#     print('C')
# elif grade >= 60 and grade <= 66:
#     print('D')
# else:
#     print('F')
# print()


# ####   ZACHS CODE    ####
# user_wants_to_continue = 'yes'
# while user_wants_to_continue == 'yes':
#     grade = int(input('Enter a number grade: '))
#     if grade >= 88:
#         print ('A')
#     elif grade >= 80:
#         print ('B')
#     elif grade >= 67:
#         print ('C')
#     elif grade >= 60:
#         print ('D')
#     elif grade >= 0:
#         print ('F')
#     print()
#     user_wants_to_continue = input('Do you want to continue? ')
#     print()



## ================================================================================ ##

# COMPLETED
# 6.  Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# MY CODE:
# book_list = [{'title': 'The Shining', 'author': 'Stephen King', 'genre': 'fiction'},
#             {'title': 'Japanese Art of Tidying', 'author': 'Marie Kondo', 'genre': 'self-help'},
#             {'title': 'Hatchet', 'author': 'Gary Paulson', 'genre': 'fiction'},
#             {'title': 'Robinson Crusoe', 'author': 'Daniel Defoe', 'genre': 'fiction'},
#             {'title': 'Stromboli Pizza: The Beastie Boys Book', 'author': 'Beastie Boys', 'genre': 'non-fiction'}]
# for feature in book_list:
#     if feature['genre'] == 'fiction' or feature['genre'] == 'self-help' or feature['genre'] == 'non-fiction':
#         print(feature['title'], ' - ', feature['author'])


# ZACH CODE:
# books = [{'title': 'The Shining', 'author': 'Stephen King', 'genre': 'fiction'},
#             {'title': 'Japanese Art of Tidying', 'author': 'Marie Kondo', 'genre': 'self-help'},
#             {'title': 'Hatchet', 'author': 'Gary Paulson', 'genre': 'fiction'},
#             {'title': 'Robinson Crusoe', 'author': 'Daniel Defoe', 'genre': 'fiction'},
#             {'title': 'Stromboli Pizza: The Beastie Boys Book', 'author': 'Beastie Boys', 'genre': 'non-fiction'}]
# genre_to_show = input('Enter a genre of book. ')
# for book in books:
#     if book['genre'] != genre_to_show:
#         continue
#     print('--------------')
#     print('- title: %s' % book['title'])
#     print('- author: %s' % book['author'])
#     print('- genre: %s' % book['genre'])
#     print('--------------')


## or...
# # Alternately, using lists in the if statement...
# books = [{'title': 'The Shining', 'author': 'Stephen King', 'genre': ['fiction', 'horror']},
#            {'title': 'Japanese Art of Tidying', 'author': 'Marie Kondo', 'genre': ['self-help', 'crazy']},
#            {'title': 'Hatchet', 'author': 'Gary Paulson', 'genre': ['fiction', 'adventure']},
#            {'title': 'Robinson Crusoe', 'author': 'Daniel Defoe', 'genre': ['fiction', 'adventure']},
#            {'title': 'Stromboli Pizza: The Beastie Boys Book', 'author': 'Beastie Boys', 'genre': ['non-fiction', 'picture']}]
# genre_to_show = input('Enter a genre of book. ')
# for book in books:
#     if genre_to_show not in book['genre']:
#         continue
#     print('--------------')
#     print('- title: %s' % book['title'])
#     print('- author: %s' % book['author'])
#     print('- genre: %s' % book['genre'])
#     print('--------------')

#####    SEE ZACH CODE FOR EXAMPLE OF HOW TO USE 'KEYS' TO DO THIS ALSO    #####
#####    VERY IMPORTANT AND HANDY... DO RESEARCH THIS !!    #####

## ================================================================================ ##

# COMPLETED
# 6.a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# # CODE:
# book_list = [{'title': 'The Shining', 'author': 'Stephen King', 'genre': 'fiction'},
#             {'title': 'The Life Changing Magic of Tidying Up', 'author': 'Marie Kondo', 'genre': 'self-help'},
#             {'title': 'Hatchet', 'author': 'Gary Paulson', 'genre': 'fiction'},
#             {'title': 'Robinson Crusoe', 'author': 'Daniel Defoe', 'genre': 'fiction'},
#             {'title': 'Stromboli Pizza: The Beastie Boys Book', 'author': 'Beastie Boys', 'genre': 'non-fiction'}]
# chosen_genre = input('Enter a book genre: ')
# for feature in book_list:
#     if chosen_genre in feature['genre']:
#         print(feature['title'], ' - ', feature['author'])

## ================================================================================ ##
##    CODE COMPLETE   ##