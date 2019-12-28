print('Type \'0\' to exit.')

x = int(input('Input value: '))

theSum = x
counter = 1

while x != 0:
    x = int(input('Input value: '))
    theSum += x
    counter += 1

print(f'The average: {theSum / (counter - 1)}.')
