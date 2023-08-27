with open("rosalind_ba2a (1).txt","r") as f:
    k, d = map(int, f.readline().strip().split())
    dna = f.readlines()
    X = [i.rstrip('\n') for i in dna]


def Hamming(string1, string2):
    h = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            h=h+ 1
    return h

def kmers(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def motivSearch(k,d,dna,kmer):
    pattern=[]
    for dn in X:
        p=set()
        for i in range(len(dn)-k+1):
            substr=dn[i:i+k]
            for km in kmer:
                if Hamming(km,substr)<=d:
                    p.add(km)
        pattern.append(p)
       
    return pattern

def inter(pattern):
    for i in range(len(pattern)) :
        if i==0:
            interse=pattern[i]

        interse = interse.intersection(pattern[i])
    return interse

kmeri=kmers(k)
pat=(motivSearch(k,d,X,kmeri))
result=inter(pat)

for res in result:
         print(res,end=' ')