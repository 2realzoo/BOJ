import sys

input = sys.stdin.readline

N, M = map(int, input().split())
unlistened = set()
unknown = []
for _ in range(N):
    unlistened.add(input())

for _ in range(M):
    unseen = input()
    if unseen in unlistened:
        unknown.append(unseen)
unknown.sort()
print(f'{len(unknown)}\n{"".join(unknown)}')