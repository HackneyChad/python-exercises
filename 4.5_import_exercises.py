# 4.5_import_exercises.py
# Hackney,_Chad
# 06 Mar 19


#====================================================================================#
# [] Exercises
# [] Create a file named 4.5_import_exercises.py to do your work in.

# [] Your "functions exercise" are not currently in a file with a name that can be easily imported.
# [] Copy your "functions exercise" file and name the copy functions_exercises.py.

# [] Import and test 3 of the functions from your "functions exercise" file.
# [] Import each function in a different way:

# [] import the module and refer to the function with the . syntax
import functions_exercises as fe
print()
fe.is_two(2)
print('import the module and refer to the function with the . syntax')
print('import functions_exercises as fe')
print('fe.is_two(2) called... All Done!')
print()

# [] use from to import the function directly
from functions_exercises import is_vowel
is_vowel("a")
print('use "from" to import the function directly')
print('from is_vowel:  is_vowel("a") called... All Done!')
print()

#  use from and give the function a different name
from functions_exercises import is_consonant as not_a_vowel
not_a_vowel("c")
print('use from and give the function a different name')
print('was: "is_consonant"... now: "not_a_vowel"')
print('from not_a_vowel:  not_a_vowel("ca") called... All Done!')
print()

#====================================================================================#
# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
import itertools
print('itertools now imported')

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import product
for i in product(['a','b','c'],[1,2,3]):
    print(i)
print('How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?')
print('source of code/reference: https://www.blog.pythonlibrary.org/2016/04/20/python-201-an-intro-to-itertools/')

# How many different ways can you combine two of the letters from "abcd"?
from itertools import permutations
for item in permutations('abcd', 2):
    print(''.join(item))
print('source of code/reference: https://www.blog.pythonlibrary.org/2016/04/20/python-201-an-intro-to-itertools/')


#==== JSON DATA PROBLEM =======================================================================#
# # Save this file (see classroom page for link to file) as profiles.json inside of your exercises directory.
# # Use the load function from the json module to open this file, it will produce a list of dictionaries.
# # Using this data, write some code that calculates and outputs the following information:

# import with json.load(open('filename'))
# # The pprint code below renders it in a legible/readable structure.
import json
from pprint import pprint
profiles = json.load(open('profiles.json'))
# [profile['index'] for profile in profiles]
# '[profile['index']... line above prints out a list of all the values identified with the 'index' key.
pprint(profiles)
print()
print('profiles.json file has finished printing!')

# Total number of users:
users = len(profiles)
print(users)

# Alterate method... Total number of users, with f-string description:
print(f'number of users: {len(profiles)}')


# active user count
import json
from pprint import pprint
profiles = json.load(open('profiles.json'))

active_count = 0
for profile in profiles:
    if profile['isActive']:
         active_count = active_count + 1
print(f'number of active users: {active_count}')
print(f'number of inactive users: {number_of_users}')
number_of_users = (len(profile_data) - (active_count))
users = len(profiles)
print(f'number ot total users: {users}')


#===================== Gary's example =====================#
# import json
# from pprint import pprint
# with open('profiles.json') as f:
#     profile_data = json.load(f)
# #  print the total number of users
# number_of_users = len(profile_data)
# print('Total number users in file profile: ',number_of_users)
 
# for user in profile_data:
#     user_id = user['_id']
#     print(user_id)     # print the user id
#     print(user.keys()) # pr
#=========================================================#

## Grand total of balances for all users:
import json
my_sum_total = 0
with open('profiles.json') as f:
    profile_data = json.load(f)

# first piece, define a variable to clean up the balance data.
print('--- Grand total of balances for all users ---')
def clean_balance(bal):
    bal = bal[1:] # remove the beginning '$'
    bal = bal.replace(',', '') # remove commas
    return float(bal)

#next piece, sum the cleaned balance data with string comprehension in for loop.
balances = [clean_balance(profile['balance']) for profile in profiles]
print(sum(balances))



# Average balance per user
# Couldn't get this one either... below is Zach's code
print('--- Average balance per user ---')
avg = sum(balances) / len(balances)
print(round(avg, 2))



# User with the lowest balance
# Couldn't get this one either... below is Zach's code
print('--- User with the lowest balance ---')
lowest = min(balances)
user = [user for user in profiles if clean_balance(user['balance']) == lowest][0]
print(user['name'])
print(round(lowest, 2))

# User with the highest balance
# applied Zach's code from above, just ran in the inverse.
print('--- User with the highest balance ---')
highest = max(balances)
user = [user for user in profiles if clean_balance(user['balance']) == highest][0]
print(user['name'])
print(round(highest, 2))
# this is the inverse of the 'lowest' code above, and generates the correct answer as the somewhat different code Zach provided in slack.



# Most common favorite fruit
# first, define a variable
print('--- Most common favorite fruit ---')
favorite_fruits = [user['favoriteFruit'] for user in profiles]

# we'll create a dictionary where the keys are the names of the fruits, and the
# values are the number of users with that fruit as their favorite
favorite_fruit_counts = {}
for fruit in favorite_fruits:
    if fruit in favorite_fruit_counts:
        favorite_fruit_counts[fruit] += 1
    else:
        favorite_fruit_counts[fruit] = 1

# Now we'll convert the dictionary to a list of key-value pairs so that we can
# sort it (dictionaries don't have an order, so they can't be sorted). We'll use
# the `sorted` function and tell it that the way we want to sort the list (using
# a lambda) is by the second item in each pair (the values, i.e. the count of
# users with that favorite fruit as their favorite). Once the list is sorted,
# the last item will be the most common favorite fruit
items = list(favorite_fruit_counts.items())
items.sort(key=lambda item: item[1])
print(items[-1][0])

print('--- Least common favorite fruit ---')
print(items[0][0])



# Total number of unread messages for all users
# My logic for approaching this problem:
# field to look at: 'greeting'
# copy code from 'balances' above and edit accordingly
  # See steps below
    # first create a define a function that: 
    # strips out anything that is not 0-9, removing all other characters
    # then it should convert that string to int
    # Then create a for loop to 
    # sum those ints

# I am unable to complete this last item tonight.  I will approach tomorrow.
# As a reference, Zach's code below.
# I had the correct or similar approach, but am unaware of how to string all this logic together.
print('--- Total number of unread messages for all users ---')
def extract_n_unread_messages(greeting: str):
    start = 'You have '
    stop = ' unread messages.'
    start_index = greeting.index(start) + len(start)
    stop_index = greeting.index(stop)
    return int(greeting[start_index:stop_index])

greetings = [user['greeting'] for user in profiles]
unread_messages = [extract_n_unread_messages(greeting) for greeting in greetings]
print(sum(unread_messages))





# #============ #
# # below is the short lecture and examples from today for working with json data files.
# # Good help below:
# this opens the file and allows it to be read as separate lines
# with open('file_name') as f:
#     lines = f.readlines()

# this replaces:  lines = contents.splt('\n')


# example:
# now combine it with the below to capture the first 10 lines
# for line in lines[:10]  # or lines[-10:]: for the last ten lines of the list
#     print(line)


# To just print the lines that are commented out code:
# for line in lines:
#     if line.startswith('#'):
#         print(line)

# this below is a list comprehension of the above:
# [print(line) for line in lines if line.startswith('#')]
# # look at the list comprehension structure and how it compares to the for loop structure above it.


# # to tell python how to interact with the file when opening it, read, write, append, create ('r', 'w', 'a', 'x')
# with open('file_name.txt', x) as f:
#     f.write('my message to display and write\n')




# # Other handy code examples below:
# #============ #
# from sys import exit
# # this tells python to import the "exit" command from the "sys" library

# filename=input('please enter a python filename: ')
# if not filename.endswith('py'):
#     print('Error: bad filename.')
#     print('      {} does not end with ".py"'.format(firstname))
#     exit()

# print('Reading file')

# # build a new list of commented out code
# commented_out_code = []
# for line in lines:
#     if line.startswith('#') or line == '':
#         commented_out_code.append(line)
#     else:
#         commented_out_code.append('# ' + line)

# print('Writing to file: {}'.format(filename))


# # below opens the file in WRITE mode, and names is as a variable 'f', then writes to the file the 'newline' character and joins it with the "commented out code" function above, to comment out every line that is not blank or already commented out.  This piece of code written into a file would allow the file to update itself.

# with open(filenname), 'w') as f:
#     f.write('\n'.join(commented_out_code))
# ============ #

#====================================================================================#
