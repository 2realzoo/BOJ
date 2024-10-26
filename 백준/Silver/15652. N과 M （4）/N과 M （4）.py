import sys
input = sys.stdin.readline
import itertools

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
nums.sort()
nums_com = itertools.combinations_with_replacement(nums, M)

for i in list(nums_com):
    for m in range(M):
        print(i[m], end=' ')
    print()
