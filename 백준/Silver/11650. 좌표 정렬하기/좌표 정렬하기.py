import sys
input = sys.stdin.readlines

t = list(map(lambda x: x.rstrip(), input()))
result = list(sorted(t[1:], key = lambda x : (int(x.split()[0]), int(x.split()[1]))))

for point in result:
    print(point)