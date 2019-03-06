# 4.4_function_practice.py
# Hackney,_Chad
# 5_Mar_19

#==============================================#
print()
print()
print('If you see this message, the file is working properly.')
print()

#==============================================#
# small assignment before break:
# def say_hello(name, greeting, punctuation):
# #    print('%s, %s%s' % (name, greeting, punctuation)) #this ONLY PRINTS in the terminal.
#     return '%s, %s%s' % (name, greeting, punctuation) #this does NOT print in the terminal, but it returns a value, that must be called in another function.

# # #this only returns the function to print to the terminal, see above.
# # say_hello('Monkey', 'we have free beer', '?')
# # print()

# print('1. Positional argument returns:')
# print(say_hello('Monkey', 'we have free beer', '?'))
# print()
# print('2. Keyword argument returns:')
# print(say_hello(punctuation = '?', greeting = 'we have free beer', name = 'Monkey'))
# print()

#==============================================#
# def say_hello(name, greeting):
#     return '{}, {}!'.format(greeting, name)

# print(say_hello('Ada', 'Greetings'))

#==============================================#
# def say_hello(name, greeting):
#     return '{}, {}!'.format(greeting, name)

# print(say_hello('Ada', 'Greetings'))

#==============================================#
# def say_hello(name, greeting):
#     return '{}, {}!'.format(greeting, name)

# name = 'Ada'
# greeting = 'Greetings'

# arguments = ['Ada', 'Greetings']

# print(say_hello(*arguments))

#==============================================#
# def say_hello(name, greeting):
#     return '{}, {}!'.format(greeting, name)

# name = 'Ada'
# greeting = 'Greetings'

# arguments = ['Ada', 'Greetings']

# print(say_hello(*arguments))
#==============================================#
# SEE ZACH CODE FOR THE SPLAT * ARGUMENTS, HOW TO IN THE DEF LINE
# PASTE THAT BELOW

#==============================================#
# KWARGS EXAMPLE... RESEARCH FURTHER, SEE ZACH CODE:
# def kwargs_example(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# kwargs_example(
#     name='Ada',
#     size=18,
#     alpha=0.05,
#     x=96
# )

# print()

#==============================================#
## RESEARCH FURTHER: see zach code for this... my code below does not work
# def makedict(**kwargs):
#     d = {}
#     for k in kwargs.keys():
#         value = kwargs[k]
#         d[k] = value
#     return d

#==============================================#
# def say_hello(greeting='hello', name='World'):
#     return f'{greeting}, {name}!'

# kwargs = {'name': 'ada', 'greeting': 'hey'}

# print(say_hello(**kwargs))

#==============================================#
# lambda function, research, but this is the syntax:
increment = lambda x: x + 1
print(increment(6))
print()
print('--------')
print()
print((lambda x: x - 1)(7))

#==============================================#
# practice done