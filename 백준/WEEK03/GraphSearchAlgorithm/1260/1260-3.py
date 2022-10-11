#DFS와 BFS

from collections import deque
import queue
import sys
from tkinter.tix import Tree


n, m, v = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(m)]

for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    nodes[tmp[0]].append(tmp[1])
    nodes[tmp[1]].append(tmp[0])
    
for i in nodes:
    nodes[i].sort()


def dfs(start_node):
    visited[start_node] = 1
    for i in range(nodes[start_node]):
        if visited[i] == 0: 
            visited[i] = 1
            dfs(i)

visited = [0] * (n + 1)
visited = [0] * (n + 1)


#큐를 만들어서 큐 안에 넣고 이동하고 넣고 이동하고 
def bfs(start_node):
    visited[start_node] = 1
    queue = deque()
    while len(queue) != 0:
        test = queue.pop()
        for i in nodes[test]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                
                
            
    
    pqueue.append(start_node)
    
    for i in range(start_node):
        
    
    
    while queue:
        
        if len(pqueue) != 0:
            pqueue.popleft()