grade = input('Input grade: ')

if grade == 'A+' or grade == 'A':
    points = 4.0
elif grade == 'A-':
    points = 3.7
elif grade == 'B+':
    points = 3.3
elif grade == 'B':
    points = 3.0
elif grade == 'B-':
    points = 2.70
elif grade == 'C+':
    points = 2.30
elif grade == 'C':
    points = 2.0
elif grade == 'C-':
    points = 1.7
elif grade == 'D+':
    points = 1.3
elif grade == 'D':
    points = 1.0
elif grade == 'F':
    points = 0
else:
    points = -1
    print('Incorrect letter grade.')

if points != -1:
    print(f'Grade points are {points}.')
