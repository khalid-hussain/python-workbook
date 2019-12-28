from math import pi, tan

n = int(input('Input n: '))
s = int(input('Input s: '))

area = (n * pow(s, 2)) / (4 * tan(pi / n))

print('Area of the regular polygon is {0:.2f}m²'.format(area))
