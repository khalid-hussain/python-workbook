from khalid_lib import getProperDivisors


def getSumOfProperDivisors(theInt):
    properDivisors = getProperDivisors(theInt)
    return sum(properDivisors)


def main():
    myInt = int(input('Input an integer: '))
    if myInt == getSumOfProperDivisors(myInt):
        print(f'Number {myInt} is a perfect number.')
    else:
        print(f'Number {myInt} is NOT a perfect number.')


if __name__ == "__main__":
    main()
