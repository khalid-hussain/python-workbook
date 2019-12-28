money = (input('Input denomination: $'))

money_faces = {
    '1': 'George Washington',
    '2': 'Thomas Jefferson',
    '5': 'Abraham Lincoln',
    '10': 'Alexandar Hamilton',
    '20': 'Andrew Jackson',
    '50': 'Ulysses S. Grant',
    '100': 'Benjamin Franklin'
}

print(money_faces[money])