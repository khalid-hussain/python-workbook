theYear = int(input('Input year: '))

leap = 'false'

if theYear % 400 == 0:
    leap = 'true'
elif theYear % 100 == 0:
    leap = 'false'
elif theYear % 4 == 0:
    leap = 'true'

if leap == 'true':
    print('It\'s a leap year.')
else:
    print('It\'s not a leap year.')
