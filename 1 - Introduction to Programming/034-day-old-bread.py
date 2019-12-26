LOAF_PRICE = 3.49
DAY_OLD_DISC = 0.6

loaves = int(input('Input no. of loaves: '))
totalPrice = loaves * LOAF_PRICE
totalPriceDiscount = totalPrice * (1 - DAY_OLD_DISC)

print('Price per loaf:       {:>5.2f}'.format(LOAF_PRICE))
print('Total price:          {:>5.2f}'.format(totalPrice))
print('Price after discount: {:>5.2f}'.format(totalPriceDiscount))
