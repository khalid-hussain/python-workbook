mpg = int(input("Input MPG: "))

liters_per_100km = mpg * 235.2145

print('{:d} mpg is {:.2f} l/100km.'.format(mpg, liters_per_100km))
