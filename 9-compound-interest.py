USURY = 0.04

amount = float(input("Money you have: "))

first_year = amount + (amount * USURY)
second_year = first_year + (first_year * USURY)
third_year = second_year + (second_year * USURY)

print('Original amount was {:.2f}. First year amount was {:.2f}. Second year amount was {:.2f}. Third year amount was {:.2f}'.format(amount, first_year, second_year, third_year))
