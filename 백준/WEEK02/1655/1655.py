# 가운데를 말해요
import heapq
import sys 

N = int(sys.stdin.readline())
heap = []
result = []

#백준이가 말한 수중에 중간값을 말해야한다. 
#백준이가 외칠 수의 개수가 짝수개 . 중간에서 작은 수를 말한다. 
for _ in range(N):
    temp = int(sys.stdin.readline().strip())

    heapq.heappush(heap, temp)
    _
    print("================")
    print(heap)

