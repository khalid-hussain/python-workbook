import string


def getAreaFromPostalCode(sPostCode):
    isPostalCode = True
    postalCodes = {'A': 'Newfoundland', 'B': 'Nova Scotia',
                   'C': 'Prince Edward Island', 'E': 'New Brunswick',
                   'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec',
                   'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario',
                   'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba',
                   'S': 'Saskatchewan', 'V': 'British Columbia',
                   'X': 'Northwest Territories or Nunavut', 'Y': 'Yukon',
                   'T': 'Alberta'}

    # The first, third and fifth characters in a Canadian postal code
    # are letters while the second, fourth and sixth characters are digits.
    # Display a meaningful error message if the postal code begins with an
    # invalid character, or if the second character in the postal code is
    # not a digit.
    if (sPostCode[0] not in string.ascii_uppercase) \
            or (sPostCode[2] not in string.ascii_uppercase) \
            or (sPostCode[5] not in string.ascii_uppercase):
        isPostalCode = False
    elif (sPostCode[1] not in string.digits) \
            or (sPostCode[4] not in string.digits) \
            or (sPostCode[6] not in string.digits):
        isPostalCode = False

    if (isPostalCode is True):
        if (sPostCode[0] not in postalCodes):
            print('Invalid Post Code. Please try again.')
        elif (sPostCode[1] == '0'):
            print(f'{postalCodes[sPostCode[0]]}, Rural Area')
        else:
            print(f'{postalCodes[sPostCode[0]]}, Urban Area')


def main():
    postalCode1 = 'T2N 1N4'
    postalCode2 = 'X0A 1B2'

    getAreaFromPostalCode(postalCode1)
    getAreaFromPostalCode(postalCode2)


if __name__ == "__main__":
    main()
