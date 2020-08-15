BASE_FARE = 4.00
FARE_PER_APPOINTED_KM = 0.25
APPOINTED_KM = 0.140


# Calculate fare for distance
# @param d distance traveled in the taxi
# @return total fare payable
def getFare(d):
    return(BASE_FARE + (d / APPOINTED_KM) * FARE_PER_APPOINTED_KM)


def main():
    theDistance = float(input('Input distance (km): '))
    print(f'The total fare is ${getFare(theDistance):,.2f}')


if __name__ == "__main__":
    main()
