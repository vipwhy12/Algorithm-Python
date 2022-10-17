# 아침 산책

# 산책과 시작과 끝점은 모두 실내여야 함
# 시작점과 끝점을 제외하고 실내 장소가 있으면 앙댐

#첫 줄에는 정점의 수 N
#둘째줄에는 1과 0으로 이루어진 길이 N의 문자열 A가 주어짐

import sys 

n = int(sys.stdin.readline())
color = list(int(sys.stdin.readline().rstrip()))

edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    first, secound = map(int, sys.stdin.readline().split())
    edges[first].append(secound)
    edges[secound].append(first)



def dfs(start):
    visited[start] = 1

    for edge in edges[start]:
        if visited[start] == 0:
            visited[start] = 1
            dfs(start)


visited = [0] * (n + 1)
count = 0


for edge in range(1, len(edges)):
    if str(color[edge - 1]) != 0:
        dfs(edges)
    count += 1
    
print(count)