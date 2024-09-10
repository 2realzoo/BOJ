import sys

input = sys.stdin.readline

N = int(input().rstrip())
n_card = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
m_card = list(map(int, input().rstrip().split()))

n_card_dict = {m:0 for m in m_card}
for n in n_card:
    if not n in n_card_dict:
        n_card_dict[n] = 1
    else:
        n_card_dict[n] += 1

result = []
for m in m_card:
    result.append(n_card_dict[m])

print(' '.join(map(str, result)))