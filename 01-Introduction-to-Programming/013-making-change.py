# Coin counter variables
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5
CENTS_PER_PENNY = 1

# Get amount of change in coins
cents = int(input('Input amount: '))

# Number of Toonies
print('{:d} Toonies.'.format(cents // CENTS_PER_TOONIE))
cents = cents % CENTS_PER_TOONIE

# Number of Loonies
print('{:d} Loonies.'.format(cents // CENTS_PER_LOONIE))
cents = cents % CENTS_PER_LOONIE

# Number of Quarters
print('{:d} Quarters.'.format(cents // CENTS_PER_QUARTER))
cents = cents % CENTS_PER_QUARTER

# Number of Dimes
print('{:d} Dimes.'.format(cents // CENTS_PER_DIME))
cents = cents % CENTS_PER_DIME

# Number of Nickels
print('{:d} Nickels.'.format(cents // CENTS_PER_NICKEL))
cents = cents % CENTS_PER_NICKEL

# Number of Pennies
print('{:d} Pennies.'.format(cents // CENTS_PER_PENNY))
cents = cents % CENTS_PER_PENNY
