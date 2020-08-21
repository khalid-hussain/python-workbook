from math import sqrt


# Calculate the hypotenuse given two sides
# @param a first side of triangle
# @param b second side of triangle
# @return c size of hypotenuse
def getHypotenuse(a, b):
    return sqrt(a**2 + b**2)


def main():
    a = int(input('Input value for a: '))
    b = int(input('Input value for b: '))
    print(f'The hypotenuse (c) is {getHypotenuse(a, b):,.2f}')


if __name__ == "__main__":
    main()
