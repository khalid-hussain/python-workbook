from math import floor

theYear = int(input('Input year: '))

theDays = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)

day_of_the_week = (theYear + floor((theYear - 1) / 4)
                   - floor((theYear - 1) / 100)
                   + floor((theYear - 1) / 400)) % 7

print(f'The day is {theDays[day_of_the_week - 1]}.')
