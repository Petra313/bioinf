with open('rosalind_ba3b.txt','r') as f:
    X = f.readlines()
    dna = [i.rstrip('\n') for i in X]


def completeDNA(dna):
    final=''
    for i in dna:
        final=final+i[0]
    final=final+i[1:]
    return final

print(completeDNA(dna))
