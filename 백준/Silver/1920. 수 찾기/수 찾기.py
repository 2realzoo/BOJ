import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = set(input().rstrip().split())
M = int(input().rstrip())
B = input().rstrip().split()

for b in B:
    if b in A:
        print('1')
    else:
        print('0')