
def HammingDistance(textA,textB):
    distance = 0
    for i,v in enumerate(textA):
        if textA[i]!=textB[i]:
            distance += 1

    return distance



if __name__=='__main__':
    filepath='/Users/skyeong/pythonwork/bioinformatics/data/dataset_9_3.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    # print (lines)
    textA = lines[0].strip()
    textB = lines[1].strip()
     
    print(HammingDistance(textA,textB))


