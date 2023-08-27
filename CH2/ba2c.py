with open('rosalind_ba2c (1).txt','r') as f:
    string=f.readline().strip()
    num=int(f.readline().strip())
    matrix =[[float(l) for l in line.strip().split()] for line in f]


def candS(string,num):
    setS=set()
    for i in range(len(string)-num+1):
        substr=string[i:i+num]
        setS.add(substr)
    return list(setS)



def cand(num,matrix,string):
    vj={}
    kandi=candS(string,num)
    for kand in kandi:
        p=1
        for i in range(num):
            if kand[i]=='A':
                p=p* matrix[0][i]
            elif kand[i]=='C':
                p=p*  matrix[1][i]
            elif kand[i]=='G':
                p=p*  matrix[2][i]
            else:
                p=p*matrix[3][i]
        vj.update({kand:p})  
        
    return vj


kandidati=cand (num,matrix,string)
max_vj=max(kandidati.values())

for k in kandidati:
    if kandidati[k]==max_vj:
        print(k)
