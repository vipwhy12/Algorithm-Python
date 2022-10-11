# 트리의 부모 찾기
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

from platform import node
import sys

N = int(sys.stdin.readline())

nodes = [[] for _ in range(N + 1)]

for i in range(N - 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    nodes[tmp[0]].append(tmp[1])
    nodes[tmp[1]].append(tmp[0])
    
def dfs(start_node):
    visited[0] = 1
    result.append(1)
    
    for i in range():
    
    for i in range(nodes):
        
    
visited = [0] * (N + 1)
result = []