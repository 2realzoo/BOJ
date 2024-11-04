import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    
    d = [[] for _ in range(2)]
    d[0].append(stickers[0][0])
    d[1].append(stickers[1][0])
    if n > 1:
        d[0].append(d[1][0] + stickers[0][1])
        d[1].append(d[0][0] + stickers[1][1])
        
        for j in range(2, n):
            d[0].append(max(d[1][j-1] , d[1][j-2]) + stickers[0][j])
            d[1].append(max(d[0][j-1], d[0][j-2]) + stickers[1][j])        
    
    print(max(d[0][n-1], d[1][n-1]))