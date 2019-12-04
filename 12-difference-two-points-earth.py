from math import radians
from math import acos, sin, cos

t1 = float(input('Input t1: '))
g1 = float(input('Input g1: '))

t2 = float(input('Input t2: '))
g2 = float(input('Input g2: '))

t1_rad = radians(t1)
g1_rad = radians(g1)

t2_rad = radians(t2)
g2_rad = radians(g2)

distance = 6371.01 * acos( sin(t1_rad) * sin(t2_rad) + cos(t1_rad) * cos(t2_rad) * cos(g1_rad - g2_rad) )

print('The distance between the two points is {:.2f}km.'.format(distance))
