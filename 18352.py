from cmath import inf
from collections import deque
import queue
import sys


n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

distance = [inf] * (n + 1)

for _ in range(m):
    first, secound = map(int, sys.stdin.readline().split())
    graph[first].append(secound)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    
    while queue:
        parent = queue.popleft()
        for p in parent:
            if visited[p] == 0:
                p.append(queue)
                visited = 1
                if distance[i] > distance[parent] + 1:
                    distance[p] = distance[parent] + 1

bfs(x)
count = 0
visited = [[0] for _ in range(n + 1)]

for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        count += 1

if count == 0:
    print(-1)
