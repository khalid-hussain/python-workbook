
def getGradePoints(grade):
    if grade == 'A+' or grade == 'A':
        return 4.00
    elif grade == 'A-':
        return 3.70
    elif grade == 'B+':
        return 3.30
    elif grade == 'B':
        return 3.00
    elif grade == 'B-':
        return 2.70
    elif grade == 'C+':
        return 2.30
    elif grade == 'C':
        return 2.00
    elif grade == 'C-':
        return 1.70
    elif grade == 'D+':
        return 1.30
    elif grade == 'D':
        return 1.00
    elif grade == 'F':
        return 0.00


theSum = 0.00
theCount = 0

while True:
    theGrade = input('Input grade: ')
    if theGrade == '':
        break
    else:
        theCount = theCount + 1
        theSum = theSum + getGradePoints(theGrade)

gpa = theSum / theCount

print(f'The grade point average is {gpa}')
