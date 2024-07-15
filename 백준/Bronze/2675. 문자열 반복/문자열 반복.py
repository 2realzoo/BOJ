import sys
input = sys.stdin.readline

t = int(input().rstrip('\n'))

for _ in range(t):
    [r, s] = input().rstrip('\n').split()
    r = int(r)
    result_str = ''
    for idx in range(len(s)):
        result_str += s[idx]*r
    
    print(result_str)