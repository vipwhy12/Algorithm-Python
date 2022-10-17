
from collections import deque
import heapq
from multiprocessing import heap
import sys


def maze(x,y):

    queue = heapq()
    queue.append((x, y))
    
    #힙큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.pop()

        #현재 방향에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #미로 공간을 벗어나?
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            #벽인 경우 바꿔!
            if graph[nx][ny] == 0:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n - 1][n - 1]
    
    
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
#이동할 네 가지 방향의 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#BFS를 수행한 결과 출력
print(maze(0, 0))
    