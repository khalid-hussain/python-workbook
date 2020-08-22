def getMean(a, b, c):
    x = a - b
    y = b - c
    z = a - c
    if (x * y) > 0:
        return b
    if (x * z) > 0:
        return c
    return a


def main():
    a = int(input('Input first integer: '))
    b = int(input('Input second integer: '))
    c = int(input('Input third integer: '))
    print(f'The median is {getMean(a, b, c)}.')


if __name__ == "__main__":
    main()
