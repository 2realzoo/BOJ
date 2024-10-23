import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for  _ in range(M)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
def bfs(queue):
    next = deque()
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and box[nx][ny] == 0:
                    next.append((nx, ny))
                    box[nx][ny] = box[x][y]+1
    return next        

q = deque()
for m in range(M):
    for n in range(N):
        if box[m][n] == 1:
            q.append((m, n))
day = -1
while q:
    q = bfs(q)
    day += 1
            
for m in range(M):
    for n in range(N):
        if box[m][n] == 0:
            day = -1

print(day)