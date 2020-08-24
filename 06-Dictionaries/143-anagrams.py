def isAnagram(strA: str, strB: str) -> bool:
    mDictOne = {}
    mDictTwo = {}
    for letter in strA:
        if mDictOne.setdefault(letter, 0):
            mDictOne[letter] = 1
        else:
            mDictOne[letter] = mDictOne[letter] + 1

    for letter in strB:
        if mDictTwo.setdefault(letter, 0):
            mDictTwo[letter] = 1
        else:
            mDictTwo[letter] = mDictTwo[letter] + 1

    if mDictOne == mDictTwo:
        return True
    else:
        return False


def main():
    myStrA = 'listen'
    myStrB = 'silent'
    print('Anagram:', isAnagram(myStrA, myStrB))


if __name__ == "__main__":
    main()
