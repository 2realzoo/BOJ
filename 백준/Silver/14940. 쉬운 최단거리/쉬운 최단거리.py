import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==-1 and map[nx][ny]==1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
for n in range(N):
    for m in range(M):
        if map[n][m] == 2 and visited[n][m] == -1:
            visited[n][m] = 0
            dfs(n, m)

for n in range(N):
    for m in range(M):
        if map[n][m] == 0:
            print(0, end=' ')
        else:
            print(visited[n][m], end=' ')
    print()
                