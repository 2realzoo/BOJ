import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def devide_num(A, B, C):
    if B == 1:
        return A % C
    else:
        k = devide_num(A, B//2, C)
        # 홀수
        if B % 2 == 1:
            return (k * k * A) % C
        # 짝수
        else:
            return (k*k)%C

print(devide_num(A, B, C))
