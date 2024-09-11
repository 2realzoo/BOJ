import sys

input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    order = input()
    if 'push' in order:
        q.append(int(order.split()[-1]))
    elif 'pop' in order:
        if len(q) > 0:
            print(q.pop(0))
        else:
            print('-1')
    elif 'size' in order:
        print(len(q))
    elif 'empty' in order:
        if len(q) > 0:
            print('0')
        else:
            print('1')
    elif 'front' in order:
        if len(q) > 0:
            print(q[0])
        else:
            print('-1')
    elif 'back' in order:
        if len(q) > 0:
            print(q[-1])
        else:
            print('-1')