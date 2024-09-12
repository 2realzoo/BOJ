import sys

input = sys.stdin.readline

N, K = map(int, input().split())

people = list(range(1, N+1))
result = []
pred_i = K-1
for i in range(N):
    if i == 0:
        result.append(str(people.pop(pred_i)))
        pred_i -= 1
    elif len(people) > pred_i + K:
        result.append(str(people.pop(pred_i + K)))
        pred_i += K -1
    else:
        pred_i = ((pred_i + K) % len(people))
        result.append(str(people.pop(pred_i)))
        pred_i -= 1
        
result = ', '.join(result)
print(f'<{result}>')