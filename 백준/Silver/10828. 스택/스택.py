import sys

input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    order = input()
    if 'push' in order:
        stack.append(int(order.split()[-1]))
    elif 'pop' in order:
        if not len(stack):
            print('-1')
        else:
            print(stack.pop())
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        if len(stack):
            print('0')
        else:
            print('1')
    elif 'top' in order:
        if not len(stack):
            print(-1)
        else:
            print(stack[-1])
