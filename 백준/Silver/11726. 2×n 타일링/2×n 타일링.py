import sys

input = sys.stdin.readline

N = int(input())
# d[1] = 1
# d[2] = 2
# d[3] = d[2]

d = {1:1, 2:2}
for n in range(3, N+1):
    d[n] = d[n-1] + d[n-2]
    
print(d[N] % 10007)