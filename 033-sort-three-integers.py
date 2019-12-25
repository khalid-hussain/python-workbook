a = int(input('Input integer a: '))
b = int(input('Input integer b: '))
c = int(input('Input integer c: '))

lowest = min(a, b, c)
highest = max(a, b, c)
middle = (a + b + c) - highest - lowest

print('Sorted Integers: {}, {}, {}'.format(lowest, middle, highest))
