

def ComputingFrequencies(Text, k):


    for i in range(4*k-1):
        FrequencyArray[i] = 0

    for i in range(len(Text)-k):
        Pattern = 
        Pattern ← Text(i, k)
        j ← PatternToNumber(Pattern)
        FrequencyArray(j) ← FrequencyArray(j) + 1
    return FrequencyArray


if __name__=='__main__':
    input_text='ACGCGGCTCTGAAA'
    k = 2

    ComputingFrequencies(input_text,k)