import sys

input = sys.stdin.readline

N = int(input())
cons = 0
for n in range(1, N):
    sum_n = n
    str_n = str(n)
    for i in range(len(str_n)):
        sum_n += int(str_n[i])
    if sum_n == N:
        cons = n
        break
print(cons)