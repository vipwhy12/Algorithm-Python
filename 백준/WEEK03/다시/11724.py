
import sys
sys.setrecursionlimit(10 ** 7)
n, m = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    edges[n1].append(n2)
    edges[n2].append(n1)
    

def dfs(start):
    visited[start] = 1
    for edge in edges[start]:
        if visited[edge] == 0:
            visited[edge] = 1
            dfs(edge)

    
count = 0    
visited = [0] * (n + 1)


for i in range(1, len(visited)):
    if visited[i] == 0:
        dfs(i)
        count +=1

print(count)