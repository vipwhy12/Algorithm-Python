# 최대 힙
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

# 입력에서 0이 주어진 회수만큼 답을 출력한다. 
# 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    
    heap_test = sys.stdin.readline()
    
    if heap_test == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(max(heap))
    
    else:
        heapq.heappush(heap,heap_test)
    

