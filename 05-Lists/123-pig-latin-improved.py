def toPigLatin(theString: list) -> list:
    myPigLatinStr = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    puncMarks = [',', '.', '?', '!']

    for word in theString:
        tPunc = ''
        tWord = word

        if word[-1] in puncMarks:
            tPunc = word[-1]
            tWord = word[0:-1]

        if tWord[0] in vowels:
            myPigLatinStr.append(tWord + 'way' + tPunc)
        else:
            for i in range(1, len(tWord)):
                if tWord[i] in vowels:
                    pStr = tWord[i:len(tWord)] + tWord[0:i] + 'ay' + tPunc
                    if tWord[0].isupper():
                        pStr = pStr[0].upper() + pStr[1:len(pStr)].lower()
                    myPigLatinStr.append(pStr)
                    break

    return myPigLatinStr


def main():
    myString = input('Input a string: ')
    myWords = myString.split()
    print(f'English  : {myWords}')
    print(f'Pig Latin: {toPigLatin(myWords)}')


if __name__ == "__main__":
    main()
