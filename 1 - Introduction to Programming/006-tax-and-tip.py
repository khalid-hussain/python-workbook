TAX = 0.05
TIP = 0.18

price = float(input("Input price of meal: "))

tax = price * TAX

tip = price * TIP

total = price + tax + tip

print('The tax is {:.2f} and the tip is {:.2f}. The total cost of meal is {:.2f}'.format(tax, tip, total))

