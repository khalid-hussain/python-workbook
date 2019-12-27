pos = input('Input position: ')

letter = pos[0]
number = int(pos[1])

if letter == 'a':
    if number % 2 == 0:
        square = 'white'
    else:
        square = 'black'
if letter == 'b':
    if number % 2 == 0:
        square = 'black'
    else:
        square = 'white'
if letter == 'c':
    if number % 2 == 0:
        square = 'white'
    else:
        square = 'black'    
if letter == 'd':
    if number % 2 == 0:
        square = 'black'
    else:
        square = 'white'
if letter == 'e':
    if number % 2 == 0:
        square = 'white'
    else:
        square = 'black'
if letter == 'f':
    if number % 2 == 0:
        square = 'black'
    else:
        square = 'white'
if letter == 'g':
    if number % 2 == 0:
        square = 'white'
    else:
        square = 'black'


print(f'Square\'s color is {square}.')
