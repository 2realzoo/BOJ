# import sys

# input = sys.stdin.readline

# N = int(input().rstrip())
# n_card = list(map(int, input().rstrip().split()))
# _ = input()
# m_card = list(map(int, input().rstrip().split()))

# n_card_dict = {m:0 for m in m_card}
# for n in n_card:
#     if not n in n_card_dict:
#         n_card_dict[n] = 1
#     else:
#         n_card_dict[n] += 1

# result = []
# for m in m_card:
#     result.append(n_card_dict[m])

# print(*result)

# 숏코드 - dictionary 활용
# import sys

# input = sys.stdin.readline

# _ = input()
# n_card = input().rstrip().split()
# d = dict.fromkeys(set(n_card), 0)

# for n in n_card:
#     d[n] += 1

# _ = input()
# m_card = input().rstrip().split()

# print(*[d.get(m, 0) for m in m_card])

# 숏코드 - Counter 활용
import sys
from collections import Counter

input = sys.stdin.readline

input()
n_card = Counter(input().split())
input()
# Counter dictionary는 누락된 항목에 대해 keyerror를 발생시키는 대신 0 반환
print(*[n_card[m] for m in input().split()])

