from collections import deque
import sys



n = int(sys.stdin.readline().rstrip())


edges = [[] for _ in range(n+1)]

for _ in range(n - 1):
    vertex1, vertex2 = map(int, sys.stdin.readline().split())
    edges[vertex1].append(vertex2)
    edges[vertex2].append(vertex1)


parent = [-1] * (n+1)

def find_parent(start):
    queue = deque()
    queue.append(start)
    parent[start] = 1
    
    while queue:
        p = queue.popleft()
        
        for edge in edges[p]:
            if parent[edge] == -1:
                queue.append(edge)
                parent[edge] = p

find_parent(1)

for i in range(2, len(parent)):
    print(parent[i])