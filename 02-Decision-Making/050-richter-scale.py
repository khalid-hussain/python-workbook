mag = float(input('Input magnitude: '))

if mag >= 10.0:
    desc = 'Meteoric'
elif mag > 7.9:
    desc = 'Great'
elif mag > 6.9:
    desc = 'Major'
elif mag > 5.9:
    desc = 'Strong'
elif mag > 4.9:
    desc = 'Moderate'
elif mag > 3.9:
    desc = 'Light'
elif mag > 2.9:
    desc = 'Minor'
elif mag > 1.9:
    desc = 'Very Minor'
else:
    desc = 'Micro'

print(f'On Richter Scale: {desc}.')
