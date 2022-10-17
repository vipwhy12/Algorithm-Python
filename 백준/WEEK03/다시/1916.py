from cmath import inf
from collections import deque
import sys

sys.stdin = open("백준/WEEK03/다시/input.txt", "r")

#n도시의 개수
#m버스의 개수

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

nodes = [[] for _ in range(n + 1)]
bus_line = [[] for _ in range(n + 1)]
distance = [inf] * (n + 1)

for i in range(m):
    first, secound, third = map(int, sys.stdin.readline().split())
    nodes[first].append(secound)
    nodes[secound].append(first)
    bus_line[first].append((secound, third))
    #distance[first].append([secound, third])

start, end = map(int, sys.stdin.readline().split())

#[[], [2, 3, 4, 5], [1, 4], [1, 4, 5], [1, 2, 3, 5], [1, 3, 4]]


print(nodes)
distance = [inf] * (n + 1)
visited = [0] * (n + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    
    while queue:
        parent = queue.popleft()
        
        for i in range():
            