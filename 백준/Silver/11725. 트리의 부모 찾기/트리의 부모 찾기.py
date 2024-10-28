import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)


while True:
    try:
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    except:
        break

q = deque()
q.append(1)

while q:
    parent = q.popleft()
    for child in graph[parent]:
        if not visited[child]:
            q.append(child)
            visited[child] = parent

for j in range(2, N+1):
    print(visited[j])
    