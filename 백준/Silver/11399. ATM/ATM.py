import sys

input = sys.stdin.readline

input()
T = sorted(list(map(int, input().rstrip().split())))
T_len = len(T)
total_t = 0
for i, t in enumerate(T):
    total_t += (T_len - i) * t

print(total_t)