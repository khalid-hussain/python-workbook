R_GAS_CONSTANT = 8.314

P = int(input('Input pressure (pascals): '))
V = int(input('Input volume (liters): '))
T_K = int(input('Input temperature (C): '))
T = T_K + 273.15

n = (P * V) / (R_GAS_CONSTANT * T)

print('Amount of gas is {0:.2f} moles'.format(n))
