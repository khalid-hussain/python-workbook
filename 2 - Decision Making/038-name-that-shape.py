n = int(input('Input no. of sides: '))

shapes = (
  'triangle',
  'quadrilateral',
  'pentagon',
  'hexagon',
  'heptagon',
  'octagon',
  'nenagon',
  'decagon')

if (n < 3 or n > 10):
    print('Number is out of range. Try again.')
else:
    print('The shape is a/an {}.'.format(shapes[n - 3]))
