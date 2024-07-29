import sys
input = sys.stdin.readlines

t = list(map(lambda x: x.rstrip(), input()))
words = sorted(list(set(t[1:])), key=lambda x : (len(x), x))
for word in words:
    print(word)