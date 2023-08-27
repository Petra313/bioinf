with open("rosalind_ba1d (1).txt","r") as f:
    pattern=f.readline().strip()
    string=f.readline().strip()

def ind(sting,pattern):
    array=[]
    for i in range(len(string)-len(pattern)+1):
        if string[i:i+len(pattern)]==pattern:
          array.append(i)
    return array


for arr in ind(string,pattern):
    print(arr,end=" ")
    



