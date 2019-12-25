height = float(input('Input height (m): '))
weight = float(input('Input weight (kg): '))

bmi = weight / (height * height)

print('The BMI is {:.2f}.'.format(bmi))
