def isAnagram(strA: str, strB: str) -> bool:
    mDictOne = {}
    mDictTwo = {}
    for letter in strA:
        if letter in mDictOne.keys():
            mDictOne[letter] = mDictOne[letter] + 1
        else:
            mDictOne[letter] = 1

    for letter in strB:
        if letter in mDictTwo.keys():
            mDictTwo[letter] = mDictTwo[letter] + 1
        else:
            mDictTwo[letter] = 1

    if mDictOne == mDictTwo:
        return True
    else:
        return False


def main():
    myStrA = 'william'
    myStrB = 'mailwil'
    print('Anagram:', isAnagram(myStrA, myStrB))


if __name__ == "__main__":
    main()
