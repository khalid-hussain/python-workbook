def reverseLookup(mDict: dict, pSearch) -> list:
    keyList = []

    if pSearch not in mDict.values():
        return keyList
    else:
        for item in mDict:
            if mDict[item] == pSearch:
                keyList.append(item)
        return keyList


def main():
    myDict = {'a': 1, 'b': 34, 'c': 29, 'd': 43, 'e': 54, 'f': 43}
    print(reverseLookup(myDict, 43))


if __name__ == "__main__":
    main()
