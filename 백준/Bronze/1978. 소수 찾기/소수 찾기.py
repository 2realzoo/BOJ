import sys
import math
input = sys.stdin.readline

n = int(input().rstrip('\n'))
nums = list(map(int, input().rstrip('\n').split()))
result = 0

for i in range(n):
    num = nums[i]
    if num == 2:
        result += 1
        continue
    for j in range(2, math.ceil(num / 2) + 1):
        if num % j == 0:
            break
        elif (j == math.ceil(num/2)) & (num % j != 0):
            result += 1

print(result)