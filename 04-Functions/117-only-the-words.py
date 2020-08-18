
def getWordsFromString(theString):
    theWords = theString.split(' ')
    theFinalWords = []
    punctuationMarks = [',', '.', '?', '-', '\'', '!', ':', ';']
    for word in theWords:
        if word[-1] in punctuationMarks:
            theFinalWords.append(word[:-1])
        else:
            theFinalWords.append(word)
    return theFinalWords


def main():
    myString = input('Enter a string: ')
    print(getWordsFromString(myString))


if __name__ == "__main__":
    main()
