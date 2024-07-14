import sys
input = sys.stdin.readline

[n, m] = map(int, input().rstrip('\n').split())
mat_n = list()
mat_m = list()

for _ in range(n):
    list_n = map(int, input().rstrip('\n').split())
    mat_n.append(list(list_n))

for _ in range(n):
    list_m = map(int, input().rstrip('\n').split())
    mat_m.append(list(list_m))

for n_idx in range(n):
    result = list()
    for m_idx in range(m):
        result.append(str(mat_n[n_idx][m_idx] + mat_m[n_idx][m_idx]))
    print(' '.join(result))