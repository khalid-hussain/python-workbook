freq = float(input('Input frequency: '))

if freq == 261.63:
    note = 'C4'
elif freq == 293.66:
    note = 'D4'
elif freq == 329.63:
    note = 'E4'
elif freq == 349.23:
    note = 'F4'
elif freq == 392.00:
    note = 'G4'
elif freq == 440.00:
    note = 'A4'
elif freq == 493.88:
    note = 'B4'
else:
    print('No note for this frequency.')
    note = 0

if (note != 0):
    print(f'The corresponding note is {note}.')
