import sys
input = sys.stdin.readline

nums = list()
for _ in range(9):
    nums.append(int(input().rstrip('\n')))

max_num = max(nums)
print(max_num)
print(nums.index(max_num)+1)