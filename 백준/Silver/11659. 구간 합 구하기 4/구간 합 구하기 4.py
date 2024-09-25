import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().rstrip().split()))

prefix = []
sum = 0
for num in nums:
    sum += num
    prefix.append(sum)
    
for _ in range(M):
    start, end = map(int, input().split())
    if start==end:
        print(nums[start-1])
    elif start==1:
        print(prefix[end-1])
    else:
        print(prefix[end-1]-prefix[start-2])
    
    
    
    