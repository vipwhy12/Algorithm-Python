# 카드2
from collections import deque
import sys

N = int(sys.stdin.readline())

cards = deque()

for i in range(1, N + 1):
    cards.append(i)
    
while(len(cards) != 1):
    cards.remove(cards[0])
    last_val = cards.popleft()
    cards.append(last_val)
    
print(cards[0])