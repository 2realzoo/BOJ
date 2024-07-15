import sys
import math
input = sys.stdin.readline

t = int(input().rstrip('\n'))
for _ in range(t):
    # 1. H W N 할당
    [h, w, n] = map(int, input().rstrip('\n').split())
    # 2. 층수
    y = n % h
    # 3. 호수
    x = math.ceil(n / h)
    # 4. 층수 + 호수
    y = str(h) if y==0 else str(y)
    x = ('0' + str(x)) if len(str(x)) == 1 else str(x)
    print(y+x)