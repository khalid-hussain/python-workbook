theOutput = []

while True:
    theWord = input('Input word: ')
    if theWord != '':
        if theWord not in theOutput:
            theOutput.append(theWord)
    else:
        break

for word in theOutput:
    print(word)
