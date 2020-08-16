
theList = []

while True:
    theInt = int(input('Insert an integer (0 to quit): '))
    if theInt != 0:
        theList.append(theInt)
    else:
        break

theList.sort()

for i in theList:
    print(i)
