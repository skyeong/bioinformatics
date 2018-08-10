
def PatternCount(Text, Pattern):
    nchar = len(Text)
    npattern = len(Pattern)
    count = 0
    for i in range(nchar):
        if Text[i:i+npattern] == Pattern:
            # print (Pattern,Text[i:i+npattern])
            count = count+1
    return count


def FrequentWords(Text, k):
    nchar = len(Text)
    Count = list()
    for i in range(nchar):
        Pattern = Text[i:i+k]
        if len(Pattern)<k:
            continue
        Count.append(PatternCount(Text,Pattern))

    maxCount = max(Count)
    FrequentPatterns = dict()
    for i in range(len(Count)):
        if Count[i] == maxCount:
            FrequentPatterns[Text[i:i+k]] = Count[i]
    print(FrequentPatterns)
  

if __name__ == '__main__':
    # filepath='/Users/skyeong/Downloads/dataset_2_10.txt'
    filepath='/Users/skyeong/Desktop/Vibrio_cholerae.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    # print (lines)
    input_text = lines[0][0:-1]
    # k = int(lines[1])
    # FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)    
    FrequentWords(input_text,5)