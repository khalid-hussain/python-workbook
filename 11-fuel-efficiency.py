mpg = int(input("Input MPG: "))

liters_per_100km = 235.2145 / mpg

print('{:d} mpg is {:.2f} l/100km.'.format(mpg, liters_per_100km))
