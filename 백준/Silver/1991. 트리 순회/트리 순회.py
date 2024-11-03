import sys

input = sys.stdin.readline

n = int(input())
graph = {}
for _ in range(n):
    node, left_child, right_child = input().split()
    graph[node] = [left_child, right_child]

def preorder(graph, visited, v):
    visited.append(v)
    for node in graph[v]:
        if not node in visited and not node=='.':
            preorder(graph, visited, node)

def inorder(graph, visited, v):
    for i, node in enumerate(graph[v]):
        if not node in visited:
            if i==0:
                if not node=='.':
                    inorder(graph, visited, node)
                visited.append(v)
            else:
                if not node=='.':
                    inorder(graph, visited, node)
    

def postorder(graph, visited, v):
    for i, node in enumerate(graph[v]):
        if not node in visited and not node=='.':
            if i==0:
                postorder(graph, visited, node)
            else:
                postorder(graph, visited, node)
    visited.append(v)

preorder_visited = []
preorder(graph, preorder_visited, 'A')
print(''.join(preorder_visited))
inorder_visited = []
inorder(graph, inorder_visited, 'A')
print(''.join(inorder_visited))
postorder_visited = []
postorder(graph, postorder_visited, 'A')
print(''.join(postorder_visited))

