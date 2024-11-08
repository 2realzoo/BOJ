import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

d = [[0]*(len(B)+1) for _ in range(len(A)+1)] 

for i, a in enumerate(A, 1):
    for j, b in enumerate(B, 1):
        if a==b:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(max(map(max, d))) 