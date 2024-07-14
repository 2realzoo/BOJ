import sys
input = sys.stdin.readline

n_num = int(input().rstrip('\n'))
n_list = map(int, input().rstrip('\n').split())
v = int(input().rstrip('\n'))

result = 0
for n in n_list:
    if v == n:
        result += 1

print(result)