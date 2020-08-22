myNumbers = []
mySum = 0

NumsBelowAverage = []
NumsAboveAverage = []
NumsAtAverage = []

while True:
    x = input('Enter an integer (blank to quit): ')
    if x == '':
        break
    else:
        myNumbers.append(int(x))
        mySum = mySum + int(x)

theAverage = mySum / len(myNumbers)

for num in myNumbers:
    if num < theAverage:
        NumsBelowAverage.append(num)
    elif num == theAverage:
        NumsAtAverage.append(num)
    elif num > theAverage:
        NumsAboveAverage.append(num)

print(f'Average: {theAverage}')
print(f'Below average values: {NumsBelowAverage}')
print(f'At average values: {NumsAtAverage}')
print(f'Above average values: {NumsAboveAverage}')
