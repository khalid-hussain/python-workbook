from math import sqrt

# m/s²
FREE_FALL_ACCELERATION = 9.8

drop_height = int(input('Drop height (m): '))

final_speed = sqrt(2 * FREE_FALL_ACCELERATION * drop_height)

print('The speed at touchdown will be {0:.2f}m/s'.format(final_speed))
