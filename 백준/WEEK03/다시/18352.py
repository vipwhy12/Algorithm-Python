

from collections import deque
from platform import node
import sys
from turtle import distance


sys.stdin = open("백준/WEEK03/다시/input.txt", "r")

#도시의 개수 N
#도로의 개수 M
#거리 정보 K
# 출발 도시 번호 X


n, m, k, x = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(n + 1)]
distance = [float('inf') for _ in range(n + 1)]

print(distance)

count = 0


for _ in range(m):
    tmp1, tmp2 = map(int, sys.stdin.readline().split())
    nodes[tmp1].append(tmp2)
    


def bfs(start):
    queue = deque()
    queue.append(start)
    distance[start] = 0
    visited[start] = 1
    
    
    global k
    
    while queue:
        tmp = queue.popleft() 
        for node in nodes[tmp]:
            queue.append()
            distance[tmp] = 1
            if visited[node] == 0:
                visited[node] = 1
                
            
            

        
    if distance == 1:
        return -1

visited = [0] * (n + 1)
print(bfs(x))
