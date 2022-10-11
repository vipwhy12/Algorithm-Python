
# 연습하기

import sys

n, m, v = map(int, sys.stdin.readline().split())

nodes = [[] for _ in range(m)]

for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[1] not in nodes[tmp[0]]:
        nodes[tmp[0]].append(tmp[1])
        nodes[tmp[1]].append(tmp[0])

for node in nodes:
    node.sort()
    
    
def dfs(start):
    visited[start] = 1
    sys.stdout.write(f'{start} ')
    
    for e in nodes[start]:
        if visited[e] == 0:
            dfs(e)


def bfs(start):
    pqueue = []
    path_2 = f'{start}'
    pqueue.append(start)
    visited[start] = 1
    
    while pqueue:
        cut = pqueue.pop(0)
        for next in edges[cur]:
            if visited[next] = 1
            path_2 += f
            

visited = [0] * (n + 1)
bfs(v)
visited = [0] * (n + 1)
