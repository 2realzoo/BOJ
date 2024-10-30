import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().rstrip().split())) for _ in range(N)]
d = [[0, 0, 0] for _ in range(N-1)]
d.insert(0, map[0])

for n in range(1, N):
    d[n][0] = map[n][0] + min(d[n-1][1], d[n-1][2])
    d[n][1] = map[n][1] + min(d[n-1][0], d[n-1][2])
    d[n][2] = map[n][2] + min(d[n-1][1], d[n-1][0])

print(min(d[N-1]))
