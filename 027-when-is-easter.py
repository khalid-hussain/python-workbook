# Double check calculations

from math import floor
import calendar

theYear = int(input('Enter year: '))

a = theYear % 19
b = floor(theYear / 100)
c = theYear % 100
d = floor(b / 4)
e = b % 4
f = floor((b + 8) / 25)
g = floor((b - f + 1) / 3)
h = ((19 * a) + b - d - g + 15) % 30
i = floor(c) / 4
k = c % 4
l = (32 + (2 * e) + (2 * i) - h - k) % 7
m = floor((a + (11 * h) + (22 * l))/451)

theMonth = floor((h + l - (7 * m) + 114) / 31)
theDate = 1 + int((h + l - (7 * m) + 114) % 31)

print('Easter in {} is on {} {}.'.format(
  theYear, theDate, calendar.month_name[theMonth]))
