myftn = {'A':0,'C':-1,'G':1,'T':0}

def MinimumSkew(input_text):
    nchar = len(input_text)
    skew = list()
    total = 0
    for i in range(nchar):
        skew.append(total)
        total += myftn[input_text[i]]

    skew.append(total)
    print(skew)
    minVal = min(skew)

    output = list()
    for i,v in enumerate(skew):
        if v==minVal: 
            output.append(i)
    return output


if __name__=='__main__':
    filepath='/Users/skyeong/pythonwork/bioinformatics/data/dataset_7_6.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    print (lines)
    input_text = lines[0][0:-1]
     
    print(MinimumSkew(input_text))