from math import sqrt

a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

discriminant = pow(b, 2) - 4 * a * c

if discriminant < 0:
    print('No real roots.')
elif discriminant == 0:
    root = -b / (2 * a)
    print(f'Root is {root}.')
elif discriminant > 0:
    root_1 = (-b + sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
    root_2 = (-b - sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
    print(f'Roots are {root_1} and {root_2}')
