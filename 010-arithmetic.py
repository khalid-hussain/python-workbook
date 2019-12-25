from math import log10

a = int(input("Input a: "))
b = int(input("Input b: "))

the_sum = a + b
the_difference = a - b
the_product = a * b
the_quotient = a / b
the_remainder = a % b
the_log10a = log10(a)
the_aPowb = a ** b

print(
'''
The sum of a and b is {:d}.
The difference when b is subtracted from a is {:d}.
The product of a and b is {:d}.
The quotient when a is divided by b is {:.2f}.
The remainder when a is divided by b is {:.2f}.
The result of log_10(a) is {:.2f}
The result of a^b is {:d}
'''.format(the_sum, the_difference, the_product, the_quotient, the_remainder, the_log10a, the_aPowb)
)