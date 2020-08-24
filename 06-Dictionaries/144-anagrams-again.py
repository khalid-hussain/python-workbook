import pprint


def isAnagram(strA: str, strB: str) -> bool:
    mDictOne = {}
    mDictTwo = {}
    mStrA = strA.lower()
    mStrB = strB.lower()

    exemptedLetters = [' ', ',', '!', '?', '.', '\'', '\"']

    for letter in mStrA:
        if letter not in exemptedLetters:
            if letter in mDictOne.keys():
                mDictOne[letter] = mDictOne[letter] + 1
            else:
                mDictOne[letter] = 1

    for letter in mStrB:
        if letter not in exemptedLetters:
            if letter in mDictTwo.keys():
                mDictTwo[letter] = mDictTwo[letter] + 1
            else:
                mDictTwo[letter] = 1

    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(mDictOne)
    # pp.pprint(mDictTwo)

    if mDictOne == mDictTwo:
        return True
    else:
        return False


def main():
    myStrA = 'William, Shakespeare?'
    myStrB = 'I am a weakish speller!'
    print('Anagram:', isAnagram(myStrA, myStrB))


if __name__ == "__main__":
    main()
