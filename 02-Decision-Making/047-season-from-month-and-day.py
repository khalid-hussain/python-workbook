theMonth = input('Input Month: ')
theDay = input('Input Day: ')

if theDay == '21':
    if theMonth == 'June':
        season = 'summer'
    elif theMonth == 'December':
        season = 'winter'
elif theDay == '20' and theMonth == 'March':
    season = 'spring'
elif theDay == '22' and theMonth == 'September':
    season = 'autumn'

print(f'The season is {season}.')
