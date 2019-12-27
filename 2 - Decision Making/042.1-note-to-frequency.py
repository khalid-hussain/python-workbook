note = (input('Input note: '))

if note == 'C4':
    freq = 261.63
elif note == 'D4':
    freq = 293.66
elif note == 'E4':
    freq = 329.63
elif note == 'F4':
    freq = 349.23
elif note == 'G4':
    freq = 392.00
elif note == 'A4':
    freq = 440.00
elif note == 'B4':
    freq = 493.88
else:
    print('Note doesn\'t exist.')
    freq = 0

if freq != 0:
    print(f'Frequency is {freq}.')
