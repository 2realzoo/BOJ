import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
per_nums = permutations(nums, M)

for num in per_nums:
    for i in range(M):
        print(num[i], end=' ')
    print()