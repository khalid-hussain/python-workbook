wl = int(input('Input wavelength: '))

if wl > 750:
    print('Wavelength is beyond visible spectrum.')
elif wl > 619:
    color = 'Red'
elif wl > 589:
    color = 'Orange'
elif wl > 569:
    color = 'Yellow'
elif wl > 494:
    color = 'Green'
elif wl > 449:
    color = 'Blue'
elif wl > 379:
    color = 'Violet'
else:
    print('Wavelength is below visible spectrum.')

print(f'Color is {color}.')
