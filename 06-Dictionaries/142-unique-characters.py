def uniqueChars(sStr: str) -> int:
    mDict = {}
    for letter in sStr:
        if mDict.setdefault(letter, 0):
            mDict[letter] = 1
            # print(f'IF mDict[{letter}]:', mDict[letter])
        else:
            mDict[letter] = mDict[letter] + 1
            # print(f'ELSE mDict[{letter}]:', mDict[letter])

    unique = 0

    for key in mDict:
        # print(f'KEY mDict[{key}]', mDict[key])
        if mDict[key] == 1:
            unique = unique + 1
            # print('unique:', unique)

    return unique


def main():
    stringOne = 'Hello, World!'
    stringTwo = 'zzz'
    print('Unique characters:', uniqueChars(stringOne))
    print('Unique characters:', uniqueChars(stringTwo))


if __name__ == "__main__":
    main()
