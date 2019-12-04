INCH_PER_FT = 12
CM_PER_INCH = 2.54

print("Input height in feet and inches")

feet = int(input("Feet: "))
inches = int(input("Inches: "))

height_in_cm = (feet * INCH_PER_FT + inches) * CM_PER_INCH

print('Your height is {:.2f} cm.'.format(height_in_cm))
