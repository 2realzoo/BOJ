import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
movie = 0
cnt = 0
while True:
    movie += 1
    if '666' in str(movie):
        cnt+=1
    if cnt == N:
        print(movie)
        break