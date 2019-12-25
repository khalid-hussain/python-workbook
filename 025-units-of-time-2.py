SECS_PER_DAY = 86400
SECS_PER_HOUR = 3600
SECS_PER_MINUTE = 60

seconds = int(input('Input seconds: '))

days = seconds // SECS_PER_DAY
seconds = seconds % SECS_PER_DAY

hours = seconds // SECS_PER_HOUR
seconds = seconds % SECS_PER_HOUR

minutes = seconds // SECS_PER_MINUTE
seconds = seconds % SECS_PER_MINUTE

print_seconds = seconds // 1

print('{:0>2}:{:0>2}:{:0>2}:{:0>2}'.format(days, hours, minutes, seconds))
