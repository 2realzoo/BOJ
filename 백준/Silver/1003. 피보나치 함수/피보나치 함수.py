import sys

input = sys.stdin.readline

T = int(input())
d = {0:[1, 0], 1:[0, 1]}
for _ in range(T):
        N = int(input().rstrip())
        result = [0, 0]
        for n in range(2, N+1):
            d[n] = [d[n-1][0]+ d[n-2][0], d[n-1][1] + d[n-2][1]]
        print(d[N][0], d[N][1])