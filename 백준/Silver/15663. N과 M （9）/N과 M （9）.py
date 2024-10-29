import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
com_nums = list(set(permutations(nums, M)))
com_nums.sort()

for com_num in com_nums:
    for m in range(M):
        print(com_num[m], end=' ')
    print()