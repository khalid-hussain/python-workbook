from math import pi

cylinder_r = int(input('Input radius: '))
cylinder_h = int(input('Input height: '))

cylinder_volume = pi * pow(cylinder_r, 2) * cylinder_h

print('Cylinder volume is {0:.1f}m²'.format(cylinder_volume))
