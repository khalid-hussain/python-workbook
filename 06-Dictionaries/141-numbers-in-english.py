# Needs testing to ensure all answers are correct
def returnNumInEng(sNum: int) -> str:
    d_Ones = {1: 'One',
              2: 'Two',
              3: 'Three',
              4: 'Four',
              5: 'Five',
              6: 'Six',
              7: 'Seven',
              8: 'Eight',
              9: 'Nine',
              10: 'Ten',
              11: 'Eleven',
              12: 'Twelve',
              13: 'Thirteen',
              14: 'Fourteen',
              15: 'Fifteen',
              16: 'Sixteen',
              17: 'Seventeen',
              18: 'Eighteen',
              19: 'Nineteen',
              20: 'Twenty'}
    d_Tens = {30: 'Thirty',
              40: 'Forty',
              50: 'Fifty',
              60: 'Sixty',
              70: 'Seventy',
              80: 'Eighty',
              90: 'Ninety'}
    d_Hundreds = {100: 'One hundred',
                  200: 'Two hundred',
                  300: 'Three hundred',
                  400: 'Four hundred',
                  500: 'Five hundred',
                  600: 'Six hundred',
                  700: 'Seven hundred',
                  800: 'Eight hundred',
                  900: 'Nine hundred'}

    theHundred = d_Hundreds[int(sNum / 100) * 100]
    t_Tens = sNum % 100
    if t_Tens > 20:
        theTen = d_Tens[int((t_Tens) / 10) * 10]
        theOne = d_Ones[int(sNum % 10)]
    else:
        theTen = d_Ones[int(sNum - (int(sNum / 100) * 100))]
        theOne = ''
    NumInWords = '%s %s %s' % (theHundred.lower(), theTen.lower(), theOne.lower())
    return NumInWords


def main():
    print(returnNumInEng(987))
    print(returnNumInEng(432))
    print(returnNumInEng(876))
    print(returnNumInEng(453))
    print(returnNumInEng(512))


if __name__ == "__main__":
    main()
