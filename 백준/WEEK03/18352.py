#특정 거리의 도시 찾기

from collections import deque
import sys
from turtle import distance

#출발 도시의 번호 
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)
visited = [False] * (n + 1)


for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])
    

def short_cut(start):
    queue = deque()
    queue.append(start)
    
    while queue:
        for i in graph[start]:
            queue.popleft()
            
        
    
    

short_cut(x)
print(graph)

visited = [0] * (n + 1)