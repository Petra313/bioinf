with open('rosalind_ba1n (5).txt','r') as f:
    pat=f.readline().strip()
    num=int(f.readline().strip())

def GenerateArray(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def Hum(x,y):
  dis=0
  for i in range(len(x)):
    if x[i]!=y[i]:
      dis=dis+1
  return dis    


niz=GenerateArray(len(pat))
for n in niz:
  if Hum(n,pat)<=num:
    print (n)