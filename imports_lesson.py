# importing


#=========================== importing from our python code library ===========================#
# example:

# time is module in the library
# sleep is a function in the time module
# i.e. the sleep function is saved on the hard drive as "py.sleep"


# import time
# # can also alias this as 'import time as t'
# # just have to update all its refrences below.

# print('Starting up...')

# time.sleep()
# # slightly delays operations, as needed: 4...3...2...1... blastoff, for example
# # aliased as 't.sleep()'

# print('All Done!')



# from time import sleep

# for n in range (10):
#     print(n)
#     sleep(0.25)




# # can also alias the 
# from time import sleep as wait

# for n in range (10):
#     print(n)
#     wait(0.25)

#=========================== importing from our own code ===========================#

can reference our own .py files

import <name of that py file, or "module">
# in python, a .py file is called a "module"

import test_sandy_code
# this references my file in the same folder as the one I'm working on.




