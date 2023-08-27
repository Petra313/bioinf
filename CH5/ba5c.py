
with open('rosalind_ba5c.txt', 'r') as f:
    A = f.readline().strip()
    B = f.readline().strip()

L = [[0 for x in range(len(A)+1)] for x in range(len(B)+1)]

for i in range(len(B)+1):
        for j in range(len(A)+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif B[i-1] == A[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

i = len(B)
j = len(A)
lcs = ''

while i > 0 and j > 0:
    if B[i-1] == A[j-1]:
        lcs+=B[i-1]
        i -= 1
        j -= 1
    elif L[i-1][j] > L[i][j-1]:
        i -= 1
    else:
        j -= 1

lcs = lcs[::-1]
print(lcs)