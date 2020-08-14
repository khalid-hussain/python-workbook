'''
dime    = 10 cents
nickel  = 5 cents
penny   = 1 cent

This question needs revision.
'''

from math import floor, ceil

theSum = 0.00

while True:
    ask = 'Input item cost (leave empty to exit): '
    tempCost = input(ask)
    if tempCost == '':
        break
    else:
        theSum = theSum + float(tempCost)

temp = (theSum * 100) % 5

if temp == 0:
    costCash = theSum
else:
    if temp < 2.5:
        costCash = floor(temp)
    else:
        costCash = ceil(temp)

print(f'Total cost: ${theSum:,.2f}')
print(f'Total cost (cash): ${costCash:,.2f}')
