import sys
input =  sys.stdin.readline
result = list(range(1,31))
for _ in range(28):
    stu = int(input().rstrip('\n'))
    result.remove(stu)

print(min(result))
print(max(result))