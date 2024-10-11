import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(visited, v):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(visited, node)

count = 0
visited = [False]*(N+1)
for n in range(1, N+1):
    if not visited[n]:
        dfs(visited, n)
        count += 1

print(count)