import sys
input = sys.stdin.readline

n = int(input().rstrip('\n'))
nums = input().rstrip('\n')
result = 0
for idx in range(len(nums)):
    result += int(nums[idx])

print(result)