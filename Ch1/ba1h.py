def Hamming(string1, string2):
    h = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            h += 1
    return h

def nofO(string, pattern, num):
    index = []
    for i in range(len(string) - len(pattern) + 1):
        substr = string[i:i + len(pattern)]
        if Hamming(substr, pattern) <= num:
            index.append(i)  # Adjust to 0-based indexing if needed
    return index

with open('rosalind_ba1h (3).txt', "r") as f:
    pattern = f.readline().strip()
    text = f.readline().strip()
    num = int(f.readline().strip())

result = nofO(text,pattern,num)
for res in result:
    print(res,end=' ')
