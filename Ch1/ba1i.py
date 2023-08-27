def kmers(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

with open('rosalind_ba1i (4).txt', "r") as f:
    pattern = f.readline().strip()
    line = f.readline().strip()  
    numbers = list(map(int, line.split()))
    k = numbers[0]
    d = numbers[1]

def Hamming(string1, string2):
    h = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            h=h+ 1
    return h


def nofO(pattern,kmer,k,d):
    kmers={}
    for i in range(len(pattern) - k + 1):
        substr = pattern[i:i + k]
        for km in kmer:
            if Hamming(substr, km) <= d:  
                if km not in kmers.keys():
                    kmers.update({km:1})
                else:
                    c=kmers[km]+1
                    kmers.update({km:c})
                    
    return kmers

kmer=kmers(k)
p=nofO(pattern,kmer,k,d)
max=max(p.values())
print(max)

for res in p:
    if p[res]==max:   
         print(res,end=' ')

