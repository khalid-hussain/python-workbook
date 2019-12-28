DISCOUNT = 0.6

prices = (4.95, 9.95, 14.95, 19.95, 24.95)

for price in prices:
    print(f'Original price: ${price:,.2f}')
    print(f'Discounted price: ${price * (1 - DISCOUNT):,.2f}')
