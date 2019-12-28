plate = input('Input license plate: ')

size = len(plate)

if size == 7:
    part1 = plate[0:4]
    # print('s7: part1', part1)
    part2 = plate[4:7]
    # print('s7: part2', part2)
    if part1.isalpha() is True and part2.isdigit() is True:
        if part1.isupper() is True:
            print('New license plate.')
        else:
            print('Incompatible plate.')
    else:
        print('Incorrect plate.')
elif size == 6:
    part1 = plate[0:3]
    # print('s6: part1', part1.isalpha())
    part2 = plate[3:6]
    # print('s6: part2', part2.isdigit())
    if part1.isalpha() is True and part2.isdigit() is True:
        if part1.isupper() is True:
            print('Old license plate.')
        else:
            print('Incompatible plate.')
    else:
        print('Incorrect plate.')
