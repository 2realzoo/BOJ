import sys
input = sys.stdin.readlines

t = list(map(lambda x: int(x.rstrip()),input()))
result = sorted(t[1:])
for i in result:
    print(i) 
