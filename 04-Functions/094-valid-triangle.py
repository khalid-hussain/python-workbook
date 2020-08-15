# Find out if three edges can form a valid triangle
# @param a first side
# @param b second side
# @param c third side
# @return boolean true if possible, false otherwise
def isValidTriangle(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        return False
    else:
        # If any one length is greater than or equal to the sum of
        # the other two then the lengths cannot be used to form a
        # triangle. Otherwise they can form a triangle.
        if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
            return False
        else:
            return True


def main():
    a = int(input('Input first side: '))
    b = int(input('Input second side: '))
    c = int(input('Input third side: '))

    print(f'Your sides create a valid triangle: {isValidTriangle(a, b, c)}')


if __name__ == "__main__":
    main()
