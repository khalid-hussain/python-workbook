from math import sqrt

s1 = int(input('Input s1: '))
s2 = int(input('Input s2: '))
s3 = int(input('Input s3: '))

s = (s1 + s2 + s3) / 2

area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print('Area of triangle is {0:.2f} m²'.format(area))
