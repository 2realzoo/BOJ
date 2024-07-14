import sys
input = sys.stdin.readline

a = input().rstrip('\n')
b = input().rstrip('\n')
c = input().rstrip('\n')
print(int(a)+int(b)-int(c))
print(int(a+b)-int(c))