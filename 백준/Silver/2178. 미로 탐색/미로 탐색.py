import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input().rstrip())))

def bfs(x, y):
    q = deque()
    q.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if miro[nx][ny]==1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))
    
    return miro[n-1][m-1]

print(bfs(0, 0))
