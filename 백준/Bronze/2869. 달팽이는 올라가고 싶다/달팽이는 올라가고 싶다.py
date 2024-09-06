import sys

input = sys.stdin.readline

A, B, V = map(int, input().rstrip().split())

days = (V - B - 1) // (A - B) + 1

print(days)