from khalid_lib import getWordsFromString


def isStringListPalindrome(theWords):
    for i in range(len(theWords)):
        theWords[i] = theWords[i].lower()
        # print(f'w: {theWords[i]}')

    theWordsReversed = list(reversed(theWords))
    # print(theWordsReversed)

    if theWords == theWordsReversed:
        return True
    else:
        return False


def main():
    myString = input('Enter a string: ')
    myWords = getWordsFromString(myString)
    # print(f'Words: {myWords}')
    print(f'Sentence is palindrome: {isStringListPalindrome(myWords)}')


if __name__ == "__main__":
    main()
