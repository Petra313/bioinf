with open('rosalind_ba1g (1).txt','r') as f:
    string1=f.readline().strip()
    string2=f.readline().strip()

def Hamming(string1,string2):
    h=0
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            h=h+1
    print(h)

Hamming(string1,string2)