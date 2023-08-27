def patternCount(text,pattern):
  count=0
  for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)] == pattern:
      count =count+1
  return count

with open("rosalind_ba1a (3).txt","r") as f:
  tekst = f.readline().strip()
  pattern = f.readline().strip()



print(patternCount(tekst,pattern))
