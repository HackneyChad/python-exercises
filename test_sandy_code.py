entry = input('Please enter a positive number: ')

while not entry.isdigit() or int(entry) <= 0:
    entry = input('Please enter a VALID POSITIVE number: ')

top_limit = int(entry) + 1
for i in range(0,top_limit):
    print (f'{i}...', end='')
print()