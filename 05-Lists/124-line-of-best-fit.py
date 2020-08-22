xValues = []
yValues = []
xyValues = []
x2Values = []

n = 0

while True:
    x = input(f'Enter value for x{n + 1} (blank to quit): ')
    if x == '':
        break
    else:
        y = input(f'Enter value for y{n + 1}: ')
        n = n + 1
        xValues.append(float(x))
        yValues.append(float(y))

sumX = sum(xValues)
sumY = sum(yValues)

for i in range(len(xValues)):
    xyValues.append(xValues[i] * yValues[i])
    x2Values.append(xValues[i]**2)

mtop = sum(xyValues) - (sum(xValues) * sum(yValues) / n)
mbottom = sum(x2Values) - (sum(xValues)**2) / (n)
m = mtop / mbottom
b = (sumX / n) - (m * (sumY / n))

print(f'Formula: y = {m:,.2f}x + {b:,.1f}')
