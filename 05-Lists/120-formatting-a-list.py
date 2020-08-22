def formatListofWords(theWords: list) -> str:
    if len(theWords) == 1:
        return theWords[0]
    elif len(theWords) == 2:
        theWords.insert(1, ' and ')
    elif len(theWords) > 2:
        theWords.insert(len(theWords) - 1, ' and ')
        for i in range(len(theWords) - 3):
            theWords.insert(i + i + 1, ', ')
    # '' means to not have any space between items
    return ''.join(theWords)


def main():
    myString = []
    while True:
        myWord = input('Type a word (blank to quit): ')
        if myWord == '':
            break
        else:
            myString.append(myWord)

    print(formatListofWords(myString))


if __name__ == "__main__":
    main()
