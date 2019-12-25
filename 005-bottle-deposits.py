ONE_LITER_DEPOSIT = 0.10
GREATER_THAN_ONE_LITER_DEPOSIT = 0.25

bottles_1L = int(input("One L bottles: "))
bottles_Greater1L = int(input("Greater than one L bottles: "))

refund = (ONE_LITER_DEPOSIT * bottles_1L) + (GREATER_THAN_ONE_LITER_DEPOSIT * bottles_Greater1L)

print("Total deposit is $%.2f." % refund)
