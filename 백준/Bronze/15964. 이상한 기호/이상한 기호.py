import sys
input = sys.stdin.readline

[a,b] = map(int, input().rstrip('\n').split())
result = (a+b)*(a-b)
print(result)