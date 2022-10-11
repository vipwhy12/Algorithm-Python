#DFS와 BFS

import sys

n, m, v = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(m)]
reult = []

for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    nodes[tmp[0]].append(tmp[1])
    nodes[tmp[1]].append(tmp[0])

for node in nodes:
    node.sort()

def dfs(start_node):
    visited[start_node] = 1
    sys.stdout.write(f'{start_node}')
    for i in nodes[start_node]:
        if visited[i] == 0: 
            visited[i] = 1
            dfs(i)

#큐를 만들어서 큐 안에 넣고 이동하고 넣고 이동하고 
def bfs(start_node):
    visited[start_node] = 1
    queue = [start_node]
    path = f'{start_node}'

    while queue:
        test = queue.pop()
        for i in nodes[test]:
            if visited[i] == 0:
                path += f'{i}'
                visited[i] = 1
                queue.append(i)
                
    print(path)    
    
visited = [0] * (n + 1)
dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)
