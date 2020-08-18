def removeOutliers(theList, n):
    theList.sort()

    for i in range(n):
        theList.pop()

    theList.reverse()

    for i in range(n):
        theList.pop()


def main():
    theCount = 0
    myList = []

    while True:
        theInt = input('Input an integer (blank to quit): ')
        if theInt == '':
            break
        else:
            theCount = theCount + 1
            myList.append(int(theInt))

    if theCount < 4:
        print('You have input less than 4 values. Try again.')
    else:
        removeOutliers(myList, 2)
        print(myList)


if __name__ == "__main__":
    main()
