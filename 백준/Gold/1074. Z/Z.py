import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

# print(2*(r%2)+(c%2)+((r+1)//2)*((c+1)//2)*(4)-4)

def zfs(N, r, c):
    if N==0:
        return 0
    return 2*(r%2)+(c%2)+ 4*zfs(N-1, r//2, c//2)

print(zfs(N, r, c))