from collections import deque
import queue
import readline
import sys


computer = int(sys.stdin.readline())
num = int(sys.stdin.readline())

edges = [[] for _ in range(computer + 1)]

for i in range(num):
    first, second = map(int, sys.stdin.readline().split())
    edges[first].append(second)
    edges[second].append(first)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    global count

    while queue:
        
        popp = queue.popleft()
        for edge in edges[popp]:
            if visited[edge] == 0:
                visited[edge] = 1
                queue.append(edge)
                count += 1
            
            
        
        
visited = [0] * (computer + 1)
count = 0
bfs(1)
print(count)