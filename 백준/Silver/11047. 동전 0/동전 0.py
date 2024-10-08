import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
result = 0
for n in range(N):
    coin = int(input())
    if coin < K:
        coins.append(coin)
    elif coin == K:
        result = 1
        break
    else:
        break
    
if result==0:
    while K > 0:
        if K >= coins[-1]:
            result += K // coins[-1]
            K %= coins[-1]
        else:
            coins.pop(-1)

print(result)