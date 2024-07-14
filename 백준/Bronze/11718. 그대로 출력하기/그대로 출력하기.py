import sys
input = sys.stdin.readlines

lines = map(lambda x: x.rstrip('\n'), input())
for line in lines:
    print(line)
