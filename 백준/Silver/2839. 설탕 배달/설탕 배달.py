import sys

input = sys.stdin.readline

n = int(input())
bags = 0
while n%5:
    if n >= 3:
        n -= 3
        bags += 1
    else:
        break
        
print((bags + n//5) if n%5==0 else -1)