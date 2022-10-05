import heapq
import sys

N = sys.stdin.readline()
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        heapq.heappush(heap, (-x, x))
    else :
        # 힙 배열이 있으면
        if len(heap) >= 1 :
            print(heapq.heappop(heap)[1])
        else:
            print(0)



