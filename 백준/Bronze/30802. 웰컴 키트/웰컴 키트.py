import sys
import math
input = sys.stdin.readline

n = int(input().rstrip('\n'))
t_sizes = list(map(int, input().rstrip('\n').split()))
[t, p] = map(int, input().rstrip('\n').split())

min_t = 0
for t_size in t_sizes:
    min_t += math.ceil(t_size / t)
print(min_t)

p_bundle = math.floor(n / p)
p_last = n % p
print(p_bundle, p_last)
