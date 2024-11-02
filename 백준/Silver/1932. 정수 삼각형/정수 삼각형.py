import sys
input = sys.stdin.readline

n =  int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*i for i in range(1, n+1)]

# 시간초과 코드
# def dfs(triangle, visited, x, y):
#     if x+1 < n:
#         left_sum = visited[x][y] + triangle[x+1][y]
#         if visited[x+1][y] < left_sum:
#             visited[x+1][y] = left_sum

#         right_sum = visited[x][y] + triangle[x+1][y+1]
#         if visited[x+1][y+1] < right_sum:
#             visited[x+1][y+1] = right_sum

#         dfs(triangle, visited, x+1, y)
#         dfs(triangle, visited, x+1, y+1)
#     else:
#         return 

# visited[0][0] = triangle[0][0]
# dfs(triangle, visited, 0, 0)
# print(max(visited[n-1]))

# dp
for i in range(1, n):
    for j in range(i+1):
        if j==0:
            triangle[i][j] += triangle[i-1][j]
        elif j==i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))