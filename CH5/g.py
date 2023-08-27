def ManhattanTourist(n,m,down,right):
    s = []
    for i in range(n + 1):
        s.append((m + 1) * [0])

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]


with open("rosalind_ba5b.txt","r")as f:
    inlines = [x.strip("\n") for x in f.readlines()]

n, m = [int(x) for x in inlines[0].split()]

down = []
for i in range(n):
    down.append([int(x) for x in inlines[1 + i].split()])

right = []
for i in range(n + 1):
    right.append([int(x) for x in inlines[n + 2 + i].split()])

print(ManhattanTourist(n, m, down, right))