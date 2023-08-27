with open('rosalind_ba2b (1).txt','r') as f:
    k=int(f.readline().strip())
    X = f.readlines()
    dna = [i.rstrip('\n') for i in X]

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

def motivSearch(k,dna,kmer):
    patterns=[]
   
    for dn in X:
        pattern={}
        for i in range(len(dn)-k+1):
            substr=dn[i:i+k]
            for km in kmer:
                c=k
                if km not in pattern.keys():
                    c=Hamming(km, substr)
                    pattern.update({km:c})

                else:
                    if Hamming(km, substr)<=pattern[km]:
                        c=Hamming(km, substr)
                        pattern.update({km:c})
                      
            
        patterns.append(pattern)
       
    return patterns


def target(pattern, inter):
    tar={}
    c=0
    for pat in pattern:
        for i in inter:
            if i not in tar.keys():
                
                tar.update({i:pat[i]})
            else:
                c=tar[i]+pat[i]
                tar.update({i:c})
               
                
    
    return tar




def inter(pattern):
    first_pat = pattern[0].keys() 
    interse = set(first_pat)  
    
    for pat in pattern[1:]:
        keys = set(pat.keys())
        interse = interse.intersection(keys)  
        
    return interse
kmeri=kmers(k)
pat=(motivSearch(k,dna,kmeri))

tar=target(pat, inter(pat))

for res in tar.keys():
    if tar[res]==min(tar.values()):
        print(res)