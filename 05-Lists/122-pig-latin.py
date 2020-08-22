
def toPigLatin(theString: list) -> list:
    myPigLatinStr = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in theString:
        # print('word[0]', word[0])
        if word[0] in vowels:
            myPigLatinStr.append(word + 'way')
        else:
            # print('Came here...')
            for i in range(1, len(word)):
                # print('word[i]', word[i])
                if word[i] in vowels:
                    pigString = word[i:len(word)] + word[0:i] + 'ay'
                    # print('pigString:', pigString)
                    myPigLatinStr.append(pigString)
                    break

    return myPigLatinStr


def main():
    myString = input('Input a string: ')
    myWords = myString.split()
    print(f'English  : {myWords}')
    print(f'Pig Latin: {toPigLatin(myWords)}')


if __name__ == "__main__":
    main()
