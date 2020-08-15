BASE_RATE = 10.95
SUBSEQUENT_ITEM_RATE = 2.95


# Get shipping charge for items
# @param numItems the total number of items
# @return the shipping charge for the items
def getShippingCharge(numItems):
    if numItems == 1:
        return BASE_RATE
    else:
        return BASE_RATE + (SUBSEQUENT_ITEM_RATE * (numItems - 1))


def main():
    noOfItems = int(input('How many items: '))
    print(f'Total shipping charge: ${getShippingCharge(noOfItems):,.2f}')


if __name__ == "__main__":
    main()
