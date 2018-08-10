def PatternCount(Text, Pattern):
    nchar = len(Text)
    npattern = len(Pattern)
    count = 0
    for i in range(nchar):
        if Text[i:i+npattern] == Pattern:
            # print (Pattern,Text[i:i+npattern])
            count = count+1
    return count


def ReverseSequences(Text):
    nText = len(Text)
    reversetext=''
    for i in range(nText):
        print (nText-i-1)
        if Text[nText-i-1] == 'A':
            reversetext = reversetext+'T'
        elif Text[nText-i-1] == 'T':
            reversetext = reversetext+'A'
        elif Text[nText-i-1] == 'C':
            reversetext = reversetext+'G'
        elif Text[nText-i-1] == 'G':
            reversetext = reversetext+'C'
    return reversetext


if __name__ == '__main__':
    filepath='/Users/skyeong/Downloads/dataset_3_2.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    print (lines)
    input_text = lines[0][0:-1]
    # k = int(lines[1])
    # FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)    
    print(ReverseSequences(input_text))