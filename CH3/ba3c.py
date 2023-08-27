with open('rosalind_ba3c (1).txt','r') as f:
    X = f.readlines()
    dna = [i.rstrip('\n') for i in X]


def createDict(dna_string):
    dictionary={}
    for dna in dna_string:
        dictionary.update({dna:''})
    return dictionary

def dictOverlap(dna):
    dic=createDict(dna)
    for d in dic.keys():
        val=[]
        for d_1 in dic.keys():
            if d[1:]==d_1[:-1]:
                val.append(d_1)
        dic.update({d:val})
    return dic
dna.sort()
result=dictOverlap(dna)

for key in result:
    if result[key]!=[]:
        print(key,end=' -> ')
        for i in result[key]:
            print(i)