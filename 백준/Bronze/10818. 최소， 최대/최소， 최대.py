import sys
input = sys.stdin.readline

n_num = int(input().rstrip('\n'))
nums = list(map(int, input().rstrip('\n').split()))
print(str(min(nums))+' '+str(max(nums)))