with open("rosalind_ba1e (1).txt","r") as f:
    string=f.readline().strip()
    line = f.readline().strip()  
    numbers = list(map(int, line.split()))
    k = numbers[0]
    L = numbers[1]
    t = numbers[2]

def kmeri(string2,k):
    kmers={}
    for i in range(len(string2)-k+1):
        kmer=string2[i:i+k]
        if kmer not in kmers.keys():
            kmers.update({kmer:1})
        else:
            c=kmers[kmer]+1
            kmers.update({kmer:c})
    return kmers

def createArr():
    strings=[]
    for i in range(len(string)-L+1):
        strings.append(string[i:i+L])
    return strings

    
arrays=createArr()
set_ans=set()
for array in arrays:
    result=kmeri(array,k)
    for res in result.keys():
        if result[res]>=t:
            set_ans.add(res)

for el in set_ans:
    print(el,end=' ')

