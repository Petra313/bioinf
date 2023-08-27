with open('rosalind_ba1l (3).txt','r') as f:
    pattern=f.readline().strip()

def pat_to_text(k,pattern):
    count=0
    c=0
    for i in pattern:
        if i=='A':
            c=0
        elif i=='C':
            c=1
        elif i=='G':
            c=2
        else:
            c=3
        count=count*4+c
    return count

print(pat_to_text(len(pattern),pattern))
