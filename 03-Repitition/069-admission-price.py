

BABY_PRICE = 0.00
CHILD_PRICE = 14.00
ADULT_PRICE = 23.00
SENIOR_PRICE = 18.00

BABY_AGE_LIMIT = 2
CHILD_AGE_LIMIT = 12
ADULT_AGE_LIMIT = 64

theCost = 0.00

while True:
    theAge = input('Input age (or blank to quit): ')
    if theAge == '':
        break
    else:
        theAge = int(theAge)
        if theAge > ADULT_AGE_LIMIT:
            theCost += SENIOR_PRICE
        elif theAge > CHILD_AGE_LIMIT:
            theCost += ADULT_PRICE
        elif theAge > BABY_AGE_LIMIT:
            theCost += CHILD_PRICE
        else:
            theCost += BABY_PRICE

print(f'The total cost of the show: ${theCost:,.2f}')
