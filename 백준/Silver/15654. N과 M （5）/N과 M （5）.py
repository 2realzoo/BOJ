import sys

input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
d = list(map(int, input().split()))
d.sort()
com_d = list(permutations(d, M))
# com_d.sort()
for i in com_d:
    for m in range(M):
        print(i[m], end=' ')
    print()
