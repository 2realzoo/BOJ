import queue
import sys

input = sys.stdin.readline
cards = [i for i in range(1,int(input().rstrip()) + 1)]
card_queue = queue.Queue(maxsize=len(cards))

for card in cards:
    card_queue.put(card)

while card_queue.qsize()>1:
    card_queue.get()
    moved_card = card_queue.get()
    card_queue.put(moved_card)

print(card_queue.get())