from calendar import isleap

theYear = int(input('Input year: '))
theMonth = int(input('Input month: '))
theDay = int(input('Input day: '))

print(f'Your date is: {theYear}-{theMonth}-{theDay}')

nextDay = ''

if theMonth == 12 and theDay == 31:
    theDay = 1
    theMonth = 1
    theYear += 1
elif theMonth in {1, 3, 5, 7, 8, 10, 12}:
    if theDay > 0 and theDay < 31:
        theDay += 1
    elif theDay == 31:
        theDay = 1
        theMonth += 1
elif theMonth in {4, 6, 9, 11}:
    if theDay > 0 and theDay < 30:
        theDay += 1
    elif theDay == 30:
        theDay = 1
        theMonth += 1
elif theMonth == 2:
    if isleap(theYear) == 'true':
        if theDay > 0 and theDay < 29:
            theDay += 1
        else:
            theDay = 1
            theMonth += 1
    else:
        if theDay > 0 and theDay < 28:
            theDay += 1
        else:
            theDay = 1
            theMonth += 1

print(f'The next date is: {theYear}-{theMonth}-{theDay}')
