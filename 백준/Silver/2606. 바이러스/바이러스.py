import sys

input = sys.stdin.readline

num = int(input())
lines = int(input().rstrip())

graph = [list() for _ in range(num+1)]
for _ in range(lines):
    com1, com2 = map(int, input().rstrip().split())
    graph[com1].append(com2)
    graph[com2].append(com1)

def dfs(graph, v, visited, result):
    visited[v] = True
    result.add(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, result)
        

visited = (num+1) * [False]
result = set()

dfs(graph,1,visited,result)
print(len(result)-1)
