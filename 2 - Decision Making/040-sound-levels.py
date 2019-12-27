sound = int(input('Input sound level (dB): '))

if sound > 130:
    result = 'Sound is louder than a jackhammer.'
elif sound == 130:
    result = 'Sound is equal to a jackhammer.'
elif sound > 106:
    result = 'Sound is between a jackhammer and gas lawnmower.'
elif sound == 106:
    result = 'Sound is equal to gas lawnmower.'
elif sound > 70:
    result = 'Sound is between a gas lawnmower and an alarm clock.'
elif sound == 70:
    result = 'Sound is equal to an alarm clock.'
elif sound > 40:
    result = 'Sound is between an alarm clock and a quiet room.'
elif sound == 40:
    result = 'Sound is equal to a quiet room.'
else:
    result = 'Sound is less than a quiet room.'

print(result)
