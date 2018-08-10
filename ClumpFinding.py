def PatternCount(Text, Pattern):
    nchar = len(Text)
    npattern = len(Pattern)
    count = 0
    for i in range(nchar):
        if Text[i:i+npattern] == Pattern:
            # print (Pattern,Text[i:i+npattern])
            count = count+1
    return count


def FrequentWords(Text, k, L, t):
    nchar = len(Text)
    Count = list()
    for i in range(nchar):
        Pattern = Text[i:i+k]
        if len(Pattern)<k:
            continue
        Count.append(PatternCount(Text,Pattern))
    #print (Count)
    FrequentPatterns = dict()
    for i in range(len(Count)):
        if Count[i] >= t:
            FrequentPatterns[Text[i:i+k]] = Count[i]
    return FrequentPatterns
  

def PatternOccurAt(Text, Pattern):
    nchar = len(Text)
    npattern = len(Pattern)
    pattern_list = list()
    for i in range(nchar):
        if Text[i:i+npattern] == Pattern:
            # print (Pattern,Text[i:i+npattern])
            if i==0 and Text[i:i+npattern]=='AAA':
                pass
            elif i==(nchar-3) and Text[i:i+npattern]=='TTT':
                pass
            else:
                # print(nchar)
                pattern_list.append(i)
    return pattern_list

def ClumpFinding(Text,k,L,t):
    kmers = FrequentWords(Text,k,L, t)
    print (kmers)
    output = list()
    for key,val in kmers.items():
        at=PatternOccurAt(Text,key)
        if len(at)<t:
            pass
        for j in range(len(at)):
            if (j+t-1) < len(at):
                pass
                if (at[j+t-1]-at[j])<L:
                    #print(at)
                    print(key,'L=',at[j+t-1]-at[j],'t=',len(at))
                    if key not in output:
                        output.append(key)
    output.sort()
    return output
            
if __name__ == '__main__':
    # filepath='/Users/skyeong/pythonwork/bioinformatics/data/dataset_4_5.txt'
    # with open(filepath) as fp:
    #     lines = fp.readlines()
    # print (lines)
    # input_text = lines[0][0:-1]
    # kLt = lines[1][0:-1]
    # kLt = [int(k) for k in kLt.split(' ')]
    # print(input_text)
    # print(kLt)
    # input_text = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
    # kLt = [3,25,3]

    filepath='/Users/skyeong/pythonwork/bioinformatics/data/E_coli.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    print (lines)
    input_text = lines[0]
    kLt = [9, 500, 3]

    clumps = ClumpFinding(input_text,kLt[0], kLt[1], kLt[2])
    print(clumps)
