theMonth = input('Input Month: ')
theDay = input('Input Day: ')

if theDay == '1':
    if theMonth == 'January':
        print('New Year\'s Day')
    elif theMonth == 'July':
        print('Canada Day')

if theDay == '25' and theMonth == 'December':
    print('Christmas Day')
