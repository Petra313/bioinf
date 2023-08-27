with open('rosalind_ba1f (4).txt','r') as f:
    genome=f.readline().strip()

def skewMin(genome):
    count=[]
    c=0
    for i in genome:
        if i=='C':
            c=c-1
        elif i=='G':
            c=c+1 
        count.append(c)
    return count

skew=skewMin(genome)
min=min(skew)

for i in range(len(skew)):
    if skew[i]==min:
        print(i+1,end=' ')   