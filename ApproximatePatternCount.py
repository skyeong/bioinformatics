
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def ApproximatePatternCount(Target,Text,maxD):
    k = len(Target)
    count = 0
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        d = HammingDistance(Target,kmer)
        if d<=maxD:
            count += 1

    return count

if __name__=='__main__':
    filepath='/Users/skyeong/pythonwork/bioinformatics/data/dataset_9_6.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
    target = lines[0].strip()
    Text = lines[1].strip()
    maxD = int(lines[2].strip())

    # target='TACAG'
    # Text='GAATCCGCCAAGTACCAAGATGTAAGTGAGGAGCGCTTAGGTCTGTACTGCGCATAAGCCTTAACGCGAAGTATGGATATGCTCCCCGGATACAGGTTTGGGATTTGGCGGTTACCTAAGCTAACGGTGAGACCGATATGACGAGGTTCCTATCTTAATCATATTCACATACTGAACGAGGCGCCCAGTTTCTTCTCACCAATATGTCAGGAAGCTACAGTGCAGCATTATCCACACCATTCCACTTATCCTTGAACGGAAGTCTTATGCGAAGATTATTCTGAGAAGCCCTTGTGCCCTGCATCACGATTTGCAGACTGACAGGGAATCTTAAGGCCACTCAAA'
    # maxD=2

    print(ApproximatePatternCount(target,Text,maxD))
