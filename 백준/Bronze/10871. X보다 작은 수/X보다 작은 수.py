import sys
input= sys.stdin.readline

[n, x] = map(int, input().rstrip('\n').split())
list_a = map(int, input().rstrip('\n').split())

result = list()
for a in list_a:
    if a < x:
        result.append(str(a))
print(' '.join(result))