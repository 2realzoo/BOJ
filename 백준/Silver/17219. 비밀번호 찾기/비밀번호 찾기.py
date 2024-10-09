import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sites = {}
for _ in range(N):
    url, password = input().rstrip().split()
    sites[url] = password

for _ in range(M):
    find_url = input().rstrip()
    print(sites[find_url])