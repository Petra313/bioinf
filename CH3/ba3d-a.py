with open('rosalind_ba3d (5).txt','r') as f:
    k=int(f.readline().strip())
    dna = f.readline().strip()

def createArr(dna_string):
    a=[]
    for i in range(0,len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        a.append(kmer)
    a.sort()    
    return a

def dictOverlap(dna):
    dic={}
    array=createArr(dna)
  

    for arr in array:
        val=''
        
        if arr[:-1] not in dic.keys():
            dic.update({(arr[:-1]):(arr[1:])})
        else:
            val=dic[arr[:-1]]+','+ arr[1:]
            
    return dic

result=dictOverlap(dna)
print(result)
with open('fi.txt', 'w') as output_file:
    for key in result:
            output_file.write(key + ' -> '+result[key])
            output_file.write( '\n')
                