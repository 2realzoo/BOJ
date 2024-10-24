import sys

input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
L = [i for i in range(1, N+1)]
com_l = list(combinations(L, M))
for i in com_l:
    for m in range(M):
        print(i[m], end=' ')
    print()

