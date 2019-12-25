V = float(input('Input wind speed (km/h): '))
T_a = float(input('Input temperature (C): '))

windChill = 13.12 + (0.6215 * T_a) - 11.37 * pow(V, 0.16) \
  + 0.3965 * T_a * pow(V, 0.16)

print('It will feel like {} C.'.format(round(windChill)))
