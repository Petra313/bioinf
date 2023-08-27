def kmers(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

with open('rosalind_ba1j (1).txt', "r") as f:
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


def revComp(pattern):
    dict={'A':'T','T':'A','C':'G','G':'C'}
    text2=''
    for s in pattern:
        if s in dict:
            text2 += dict[s]
            
    return text2[::-1]

kmer=kmers(k)
pattern2=revComp(pattern)
p=nofO(pattern,kmer,k,d)
r=nofO(pattern2,kmer,k,d)
result={}
for key in p.keys():
    if key in r.keys():
        re=p[key]+r[key]
        result.update({key:re})
max=max(result.values())
print(max)

for res in result:
    if result[res]==max:   
         print(res,end=' ')

