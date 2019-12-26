from math import pi

r = float(input('Input radius (m): '))

area = pi * r * r
volume = 4/3 * pi * r ** 3

print('Area is {:.2f} m^2.'.format(area))
print('Volume is {:.2f} m^3.'.format(volume))
