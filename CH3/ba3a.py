with open('rosalind_ba3a (1).txt','r') as f:
    k=int(f.readline().strip())
    string=f.readline().strip()


def composition(k,string):
    kmer=[]
    for i in range(len(string)-k+1):
        substr=string[i:i+k]
        kmer.append(substr)
    
    return kmer


result=composition(k,string)
result.sort()
print(result)
for res in result:
    print(res)
