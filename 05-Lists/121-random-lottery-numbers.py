import random


def getSixRandomNumbers() -> list:
    theNumbers = []
    while len(theNumbers) < 6:
        x = random.randrange(1, 50)
        # print(f'x: {x}')
        if x not in theNumbers:
            theNumbers.append(x)

    theNumbers.sort()
    return theNumbers


def main():
    print(getSixRandomNumbers())


if __name__ == "__main__":
    main()
