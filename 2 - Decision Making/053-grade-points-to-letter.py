points = float(input('Input points: '))

if points >= 4.00:
    letter = 'A+'
elif points >= 3.7:
    letter = 'A'
elif points >= 3.3:
    letter = 'B+'
elif points >= 3.0:
    letter = 'B'
elif points >= 2.7:
    letter = 'B-'
elif points >= 2.3:
    letter = 'C+'
elif points >= 2.0:
    letter = 'C'
elif points >= 1.7:
    letter = 'C-'
elif points >= 1.3:
    letter = 'D+'
elif points >= 1.0:
    letter = 'D'
elif points >= 0:
    letter = 'F'

print(f'Grade is {letter}.')
