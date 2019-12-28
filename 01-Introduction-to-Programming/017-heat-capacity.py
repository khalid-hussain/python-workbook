# I'm not sure about the validity of this answer

# J per gram Celsius
HEAT_CAP_WATER = 4.186

mass = int(input('Mass in grams: '))
temp_change = int(input('Temp. change in celsius: '))

# Energy required, q = mCΔT
q = mass * HEAT_CAP_WATER * temp_change
total_kWh = q/3600000
cost = total_kWh * 8.9

print('Energy required is {}j'.format(int(q)))
print('Cost of energy is ${0:.2f}'.format(cost))