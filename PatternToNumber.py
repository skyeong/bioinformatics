NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
SymbolToNumber = {'A':0, 'C':1, 'G':2, 'T':3}


def PatternToNumber(Text):
    nchar = len(Text)
    num = 0
    for i in range(nchar):
        num += pow(4,nchar-SymbolToNumber[i]-1)*SymbolToNumber[i]
    return num

if __name__ == '__main__':
    input_text='ATGCAA'
    print(PatternToNumber(input_text))
