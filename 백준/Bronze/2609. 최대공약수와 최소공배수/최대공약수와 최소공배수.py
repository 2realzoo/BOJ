import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

min_num = min(a, b)
max_num = max(a, b)

com_div = 0
for i in range(min_num, 0, -1):
    if (max_num % i == 0) and (min_num % i == 0):
        com_div = i
        break

a_div = a / com_div
b_div = b / com_div
com_mul = a_div * b_div * com_div

print(com_div)
print(int(com_mul))