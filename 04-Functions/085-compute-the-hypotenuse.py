from math import sqrt


def getHypotenuse(a, b):
    return sqrt(a**2 + b**2)


def main():
    a = int(input('Input value for a: '))
    b = int(input('Input value for b: '))
    print(f'The hypotenuse (c) is {getHypotenuse(a, b):,.2f}')


if __name__ == "__main__":
    main()
