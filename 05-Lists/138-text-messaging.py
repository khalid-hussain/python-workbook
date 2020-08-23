def t9Lookup(mWord) -> str:
    t9Dict = {'1': ['.', ',', '?', '!', ':'],
              '2': ['A', 'B', 'C'],
              '3': ['D', 'E', 'F'],
              '4': ['G', 'H', 'I'],
              '5': ['J', 'K', 'L'],
              '6': ['M', 'N', 'O'],
              '7': ['P', 'Q', 'R', 'S'],
              '8': ['T', 'U', 'V'],
              '9': ['W', 'X', 'Y', 'Z'],
              '0': [' ']}

    t9DictTwo = {'.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
                 'A': '2', 'B': '22', 'C': '222',
                 'D': '3', 'E': '33', 'F': '333',
                 'G': '4', 'H': '44', 'I': '444',
                 'J': '5', 'K': '55', 'L': '555',
                 'M': '6', 'N': '66', 'O': '666',
                 'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
                 'T': '8', 'U': '88', 'V': '888',
                 'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
                 ' ': '0'}

    returnString = ''

    for letter in mWord:
        # print(letter, t9DictTwo[letter.upper()])
        returnString = returnString + t9DictTwo[letter.upper()]

    return returnString


def main():
    mString = 'Hello, World!'
    print(t9Lookup(mString))


if __name__ == "__main__":
    main()
