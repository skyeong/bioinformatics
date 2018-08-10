

def PatternCount(Text, Pattern):
    nchar = len(Text)
    npattern = len(Pattern)
    count = 0
    for i in range(nchar):
        if Text[i:i+npattern] == Pattern:
            # print (Pattern,Text[i:i+npattern])
            count = count+1
    return count

if __name__ == '__main__':
    filepath='/Users/skyeong/Downloads/dataset_2_7.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    input_text = lines[0][0:-1]
    test_seq = lines[1][0:-1]

    print(PatternCount(input_text,test_seq))