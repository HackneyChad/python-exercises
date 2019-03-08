# 4.5_working_with_files.py 
# Hackney,_Chad 
# 07 Mar 19 
#==============#



#================================ EXERCISES ================================#
# # Exercises
# # Read the contents of your last exercise file into a variable.

# # Print out every line in the file
# # # this opens the file and allows it to be read as separate lines
from pprint import pprint
with open('4.5_import_exercises.py','r') as f:
    lines = f.readlines() # both "lines = ..."" and
    pprint(lines)         # "pprint" print out the file contents, run both and see

# # Print out every line in the file, but add line numbers
with open('4.5_import_exercises.py', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines, start=1):
       print('{} = {}'.format(i+1, line.strip()))

#  running those two snippets of code above simultaneously results in five separate print outs of this data.  Why?


# Per Zach, moving on now, back to the previous (import) lesson re json data.
# Then I'll circle back to this one below.



# # Write some python code to create a grocery list.
# # Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 3 things that you need to buy from the grocery store.

grocery_list = ['bread', 'milk', 'butter']

# Create a function named make_grocery_list.
# When run, this function should write the contents of the grocery_list variable
# to a file named my_grocery_list.txt.

def make_grocery_list():
     f.write((grocery_list)[0,1,2])
     is it possible to use function parameters here in the write statement instead of strings?


grocery_list = ['bread', 'milk', 'butter']
with open('file_name.txt', x) as f:
     f.write((grocery_list)[0,1,2])
print(make_grocery_list)




# Create a function named show_grocery_list. When run, it should show each item on the grocery list.



# Create a function named buy_item. It should accept the name of an item on the grocery list, and remove that item from the list.