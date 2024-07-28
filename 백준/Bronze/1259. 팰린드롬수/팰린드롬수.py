import sys
import math
input = sys.stdin.readlines

t = list(map(lambda x: list(x.rstrip()), input()))
for nums in t:
    if nums[0] == '0':
        break
    
    n = len(nums)
    result = True
    if nums[0]:
        for idx, num in enumerate(nums[:math.floor(n/2)]):
            if not num == nums[n-1-idx]:
                result = False
                
        if result:
            print('yes')
        else:
            print('no')

    