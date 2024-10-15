import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)
while start <= end:
    mid = (start+end)//2
    log = 0
    for i in trees:
        if i >= mid:
            log += i - mid
    
    if log >= M:
        start = mid + 1
    elif log < M:
        end = mid -1

print(end)