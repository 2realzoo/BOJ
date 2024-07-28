import sys
input = sys.stdin.readline

N = int(input().rstrip())
scores = list(map(int, input().rstrip().split()))
M = max(scores)
result = 0

for score in scores:
    result += score/M*100
    
print(result/N)