negatives = []
zeroes = []
positives = []

while True:
    theNumber = input('Input an integer: ')
    if theNumber != '':
        theNumber = int(theNumber)
        if theNumber == 0:
            zeroes.append(theNumber)
        elif theNumber > 0:
            positives.append(theNumber)
        elif theNumber < 0:
            negatives.append(theNumber)
    else:
        break

theMegaList = negatives + zeroes + positives

for integer in theMegaList:
    print(integer)
