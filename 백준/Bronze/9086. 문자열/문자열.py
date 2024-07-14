import sys
input = sys.stdin.readline
t = int(input().rstrip('\n'))

for i in range(t):
    str = input().rstrip('\n')
    print(str[0]+str[-1])