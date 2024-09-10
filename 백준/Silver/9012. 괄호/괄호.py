import sys

input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    ps = input().rstrip()
    open = 0
    done = False
    for _, p in enumerate(ps):
        if p == '(':
            open += 1
        elif open:
            open -= 1
        else:
            print('NO')
            done = True
            break
    if done:
        continue
    elif not open:
        print('YES')
    elif open:
        print('NO')