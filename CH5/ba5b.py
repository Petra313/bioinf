with open("rosalind_ba5b (2).txt","r")as f:
    inlines = [x.strip("\n") for x in f.readlines()]

n, m = [int(x) for x in inlines[0].split()]

down = []
for i in range(n):
    down.append([int(x) for x in inlines[1 + i].split()])

right = []
for i in range(n + 1):
    right.append([int(x) for x in inlines[n + 2 + i].split()])


def mt(n,m,Down,Right):
    s = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0]=s[i-1][0]+Down[i-1][0]
    for j in range(1,m+1):
        s[0][j]=s[0][j-1]+Right[0][j-1]
    for i in range(1,n+1):
            for j in range(1,m+1):
                 s[i][j]=max( s[i-1][j]+Down[i-1][j], s[i][j-1]+Right[i][j-1])
                 
    print(s[n][m])

mt(n,m,down,right)
