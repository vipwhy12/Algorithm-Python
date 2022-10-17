#바이러스

from platform import node
import sys


computer = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
count = 0
nodes = [[] for _ in range(computer + 1)]

for i in range(edges):
    tmp = list(map(int, sys.stdin.readline().split()))
    nodes[tmp[0]].append(tmp[1])
    nodes[tmp[1]].append(tmp[0])

def dfs(start_node):
    global count
    visited[1] = 1
    for next in nodes[start_node]:
        if visited[next] == 0:
            visited[next] = 1
            count += 1
            dfs(next)
            
visited = [0] * (computer + 1)

dfs(1)
print(count)