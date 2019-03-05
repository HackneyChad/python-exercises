# 4.2_control_structures_practice.py
# Hackney, Chad
# 4 Mar 19

print()
print('## ========================================= ##')
print()
# file test:
print('This will print if the file works...')


# 1. prompt the user for a day of the week, print out whether the day is Monday
#    or not

# look at Zach's example codeon the Git page

# weekday = input('Please enter a weekday: ')
# print(f'weekday = {weekday}')
# if weekday == 'Monday':
#     print('Sounds like someone has a case of the Mondays!')
# else:
#     print('It is NOT Monday')



# 2. prompt the user for a day of the week, print out whether the day is a
#    weekday or a weekend

# weekday = input('Please enter a day fo the week: ')
# if weekday.lower().startswith('s'):
#     print('It is a weekend!')
# else:
#     print('It is NOT a weekend.')

# weekend_days = ['saturday', 'sunday']
# weekday = input


# 3. create variables and make up values for
#
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

#  My work, sample code below:

# hours_worked = 43
# hourly_rate = 900
# if hours_worked > 40:
#     pay_at_regular_rate = 40 * hourly_rate
#     overtime_pay = (hours_worked - 40) * hourly_rate *1.5
#     paycheck = pay_at_regular_rate + overtime_pay
# else:
#     paycheck = hourly_rate * hours_worked

# print(paycheck)


## ============================================== ##
# Loops section below:
# print
# for n in range(1, 11):
#     print(n)


## ============================================== ##

# languages = ['bash', 'python', 'R', 'clojure']

# for programming_language in languages:
#     if programming_language == 'python':
#         print(f'{programming_language} is my favorite!')
#     else:
#         print(f'{programming_language} is a nice programming language')

## ============================================== ##

print()
# while loop example:
i = 5
while i <= 12:
    print(i)
    i += 1

## ============================================== ##
print()








