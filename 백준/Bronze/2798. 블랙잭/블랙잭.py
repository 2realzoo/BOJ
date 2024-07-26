import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
cards = sorted((map(int, input().rstrip().split())), reverse=True)

max = 0

for idx1, card1 in enumerate(cards):
    if card1 >= M :
        continue
    for idx2 in range(idx1+1,N):
        card2 = cards[idx2]
        if card1 + card2 >= M:
            continue
        for idx3 in range(idx2+1,N):
            card3 = cards[idx3]
            if M >= card1 + card2 + card3 > max:
                max = card1 + card2 + card3
            
print(max)
            