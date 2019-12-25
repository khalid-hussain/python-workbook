pressure = float(input('Input pressure (kilo-pascals): '))

poundsPerInchSquare = pressure * 0.145

mmHg = pressure / 0.1333223684

atm = pressure / 101.325

print('Pressure in pounds per square inch is {:.2f}.'.format(
  poundsPerInchSquare))
print('Pressure in millimeter mercury is {:.2f}.'.format(mmHg))
print('Pressure in atmospheres is {:.2f}.'.format(atm))
