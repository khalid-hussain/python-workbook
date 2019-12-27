a = int(input('Input side a: '))
b = int(input('Input side b: '))
c = int(input('Input side c: '))

if a == b == c:
    print('Triangle is equilateral.')
elif a == b or a == c or c == b:
    print('Triangle is isosceles.')
else:
    print('Triangle is scalene.')
