def kmers(text,k):
  array=[]
  for i in range(len(text)-k+1):
    kmer=text[i:i+k]
    array.append(kmer)
  return array

def patternCount(text,pattern):
  count=0
  for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)] == pattern:
      count =count+1
  return count

def countKmers(text,array):
   dict={}
   for kmer in array:
      c=patternCount(text,kmer)
      dict.update({kmer:c})
   a= [k for k, v in dict.items() if v == max(dict.values())]
   return a


with open("rosalind_ba1b (1).txt","r") as f:
  tekst = f.readline().strip()
  k= f.readline().strip()

res=countKmers(tekst,kmers(tekst,int(k)))
for r in res:
  print(r,end=" ")
