import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().rstrip().split()))
dict_X = {}
sorted_X = sorted(list(set(X)))
for i, x in enumerate(sorted_X):
    if not x in dict_X:
        dict_X[x] = i
result = []
for x in X:
    result.append(str(dict_X[x]))

print(' '.join(result))
