#카드 정렬하기


import heapq
import sys

n = int(sys.stdin.readline())
cards = []

for i in range(n - 1):
    cmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards.cmp)
    sum += cmp
print(sum)