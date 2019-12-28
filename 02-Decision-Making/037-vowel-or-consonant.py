letter = input('Input letter: ')

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

if (letter in vowels):
    print('Letter is a vowel.')
elif (letter == 'y' or letter == 'Y'):
    print('y is sometimes a consonant and sometimes a vowel.')
else:
    print('Letter is a consonant.')
