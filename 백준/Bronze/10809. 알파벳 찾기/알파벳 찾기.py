import sys
input = sys.stdin.readline

s = input().rstrip('\n')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = list()
for a in alphabet:
    result.append(str(s.find(a)))
print(' '.join(result))