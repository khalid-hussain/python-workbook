h = int(input('Input human years: '))
d = 0

if (h < 0):
    print('Input is negative! Try again.')
else:
    if (h <= 2):
        d = h * 10.5
    else:
        # d = (2 * 10.5) + ((h - 2) * 4)
        d = 4 * (5.25 + h - 2)

print('The age in dog years is {:.1f}'.format(d))
