freq = float(input('Input frequency: '))

if freq < 3 * pow(10, 9):
    em = 'Radio Waves'
elif freq < 3 * pow(10, 12):
    em = 'Microwaves'
elif freq < 4.3 * pow(10, 14):
    em = 'Infrared Light'
elif freq < 7.5 * pow(10, 14):
    em = 'Ultraviolet Light'
elif freq < 3 * pow(10, 17):
    em = 'X-Rays'
elif freq >= 3 * pow(10, 19):
    em = 'Gamma Rays'

print('Electromagnetic Radition: {em}.')
