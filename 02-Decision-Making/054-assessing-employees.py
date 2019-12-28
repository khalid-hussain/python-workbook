EMPLOYEE_RAISE = 2400

rating = float(input('Input rating: '))

if rating == 0.0:
    print('Unacceptable Performance.')
elif rating == 0.4:
    print('Acceptable Performance.')
elif rating == 0.6:
    print('Meritorious Performance.')

print(f'Employee raise is ${rating * EMPLOYEE_RAISE:,.2f}.')
