for x in range(1, 101):
    if x % 3 == 0:
        if x % 5 == 0:
            print(f'{x} Fizz Buzz')
        else:
            print(f'{x} Fizz')
    elif x % 5 == 0:
        print(f'{x} Buzz')
    else:
        print(f'{x}')
