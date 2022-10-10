
from collections import deque
import sys


node, edge, start_node  = map(int, sys.stdin.readline().split())

# 사용자가 입력할 리스트를 담을 arr
arr = []

# 사용자가 입력한 tree arr
tree = [[] for _ in range(node + 1)]

#방문했는지 확인하는 arr
visited = [0 for _ in range(node + 1)]
result = []

#사용자가 입력한 노드 관계들을 arr에 넣어줍니다. 
for i in range(edge):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(arr)):
    tree[arr[i][0]].append(arr[i][1])    
    tree[arr[i][1]].append(arr[i][0])


def dfs(start_node):
    if visited[start_node] == 0:
        result.append(start_node)
        visited[start_node] = 1
    
    for i in tree[start_node]:
        if visited[i] == 0:
            visited[i] = 1
            result.append(i)
            dfs(i)
        elif visited == 1:
            continue


def bfs(star_node):
    
    #a sh노드를 방문한다 
    #초기 상태에 큐에서는 시작 노드만 저장 
    
    q = deque()
    q.append(star_node)
    
    if start_node == 0:
        q.append(arr)
    for i in range():
    
    
dfs(start_node)


print(result)