import sys
input = sys.stdin.readline

t = int(input())

result = list()
for _ in range(t):
    [a,b] = map(int, input().rstrip('\n').split())
    result.append(str(a+b))

for i in range(len(result)):
    print(result[i])