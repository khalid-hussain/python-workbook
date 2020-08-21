# From Question 115
def getProperDivisors(theInt):
    n = theInt - 1
    properDivisors = []
    while n > 0:
        if theInt % n == 0:
            properDivisors.append(n)
        n = n - 1
    return properDivisors


def main():
    print("Main function")


if __name__ == "__main__":
    main()
