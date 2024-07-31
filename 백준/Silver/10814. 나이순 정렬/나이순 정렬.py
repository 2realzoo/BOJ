import sys
input = sys.stdin.readlines

t = list(map(lambda x: x.rstrip(), input()))

members = sorted(t[1:], key = lambda x: int(x.split()[0]))

for member in members:
    print(member)
