# This question might need revision

def isListSorted(theList: list) -> bool:
    flagSorted = False
    for i in range(len(theList) - 1):
        if theList[i + 1] > theList[i]:
            flagSorted = True
        else:
            flagSorted = False
            break
    return flagSorted


def main():
    myList = []
    while True:
        x = input('Enter integer (blank to quit): ')
        if x == '':
            break
        else:
            myList.append(int(x))
    print(f'List is sorted: {isListSorted(myList)}')


if __name__ == "__main__":
    main()
