days = int(input('Input Days: '))
hours = int(input('Input Hours: '))
minutes = int(input('Input Minutes: '))
seconds = int(input('Input Seconds: '))

total_seconds = seconds + (minutes * 60) + (hours * 3600) + (days * 24 * 3600)

print('Total time is {} seconds.'.format(total_seconds))
