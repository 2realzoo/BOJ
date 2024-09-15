import sys

input = sys.stdin.readline

N , M = map(int, input().rstrip().split())
board = []
for n in range(N):
    row = list(map(lambda x: x, input().rstrip()))
    board.append(row)
# 처음이 w인 경우와 b인 경우로 나누어 repaint 확인
repaint_list = []
for n in range(N-7):
    for m in range(M-7):
        repaint_w = 0
        repaint_b = 0
        # 8*8자른 것 내부 확인
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    cur = board[n+i][m+j]
                    if not cur == 'W':
                        repaint_w += 1
                    if not cur == 'B':
                        repaint_b += 1
                else:
                    cur = board[n+i][m+j]
                    if not cur == 'B':
                        repaint_w += 1
                    if not cur == 'W':
                        repaint_b += 1
        repaint_list.append(min(repaint_b, repaint_w))
print(min(repaint_list))