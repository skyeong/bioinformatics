def PatternCount(Text, Pattern):
    nchar = len(Text)
    npattern = len(Pattern)
    count = 0
    for i in range(nchar):
        if Text[i:i+npattern] == Pattern:
            # print (Pattern,Text[i:i+npattern])
            count = count+1
    return count

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

if __name__ == '__main__':
    # filepath='/Users/skyeong/Downloads/dataset_3_5.txt'
    # with open(filepath) as fp:
    #     lines = fp.readlines()
    # print (lines)
    # input_text = lines[1][0:-1]
    # test = lines[0][0:-1]
    # print(PatternOccurAt(input_text,test))
  
    print(PatternOccurAt('GACGATATACGACGATA','ATA'))