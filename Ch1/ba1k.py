with open('rosalind_ba1k (1).txt','r') as f:
    pattern=f.readline().strip()
    num=int(f.readline().strip())

def kmers(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def freq(pattern,kmer,k):
    kmers={}
    for i in range(len(pattern) - k + 1):
        substr = pattern[i:i + k]
        for km in kmer:
            if km==substr:    
                if km not in kmers.keys():
                    kmers.update({km:1})
                else:
                    c=kmers[km]+1
                    kmers.update({km:c})
            else:
                if km not in kmers.keys():
                    kmers.update({km:0})
                    
    return kmers

kmeri=kmers(num)
freqarr=freq(pattern,kmeri,num)

for fa in freqarr:
    print(freqarr[fa],end=' ')
