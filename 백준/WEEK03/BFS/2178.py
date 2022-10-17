#미로 탐색
from collections import deque
import sys

#BFS로 미로를 탈출하자
def maze_exit(x, y):
    
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    
    #큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()

        #현재 방향에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]
    
    
#N, M 공백을 기준으로 구분하여 입력받기
n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
#이동할 네 가지 방향의 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS를 수행한 결과 출력
print(maze_exit(0, 0))