import sys
from collections import deque

sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(v):
    seen[v] = True
    dfs_result.append(str(v))
    for i in graph[v]:
        if not seen[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    seen[start] = True
    
    while queue:
        v = queue.popleft()
        bfs_result.append(str(v))
        
        for i in graph[v]:
            if not seen[i]:
                queue.append(i)
                seen[i] = True
            
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for n in range(1, N+1):
    graph[n].sort()

seen = [False] * (N+1)
dfs_result = []
dfs(V)

seen = [False] * (N+1)
bfs_result = []
bfs(V)

print(' '.join(dfs_result))
print(' '.join(bfs_result))
