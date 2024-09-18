import sys

input = sys.stdin.readline

N = int(input())

d = {1:0}

# greed 알고리즘 - 거스름돈 문제(단순 큰 것부터 계산)하는 것과 구분할 것
# DP 알고리즘 - 문제를 작게 쪼개기

for n in range(2, N+1):
    d[n] = d[n-1] + 1
     
    if not n%2 and d[n//2] < d[n]:
        d[n] = d[n//2] + 1
        
    if not n%3 and d[n//3] < d[n]:
        d[n] = d[n//3] + 1

print(d[N])
