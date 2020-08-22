# Consider revising answer
def countRange(argList: list, argMin, argMax) -> int:
    returnStr = []
    returnInt = 0
    for num in argList:
        if num >= argMin and num < argMax:
            returnInt = returnInt + 1

    return returnInt


def main():
    listA = [4, 5, 3, 2, 3, 99, 45]
    listB = [1, 43, 22, 98, 54, 44, 33]
    listC = [12, 54, 36, 72, 92, 101, 65]

    print('ListA: ', countRange(listA, 4, 50), 'numbers.')
    print('ListB: ', countRange(listB, 45, 50), 'numbers.')
    print('ListC: ', countRange(listC, 30, 50), 'numbers.')


if __name__ == "__main__":
    main()
