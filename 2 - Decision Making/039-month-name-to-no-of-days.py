theMonth = input('Input Month (MMM): ')

days = 31

if theMonth == 'FEB':
    days = '28 or 29'
elif theMonth == 'FEB' or theMonth == 'APR' or theMonth == 'JUN' or \
  theMonth == 'SEP' or theMonth == 'NOV':
    days = 30

print('There are {} days in {}'.format(days, theMonth))
