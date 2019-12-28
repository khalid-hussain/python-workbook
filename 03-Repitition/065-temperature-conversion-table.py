
cel = 0

print('Celsius  |  Farenheit')
print('------------------------')

for x in range(0, 110, 10):
    print(f'   {x:3d}   |  {x * 1.8 + 32:.2f}')
