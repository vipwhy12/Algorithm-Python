from collections import deque
import sys


n = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
visited = [[0] * n] * n

#아파트 단지의 수를 저장할 리스트
apartment = []

#단지의 개수를 카운트할 개수
count = 0

for i in range(n):
    graph[i] = list(map(int, list(sys.stdin.readline().strip())))
    
    

def bfs(x, y):
    # 행렬에 인접한 곳에 아파트가 있는지 없는지 확인하자 
    direct_x = [0, 0, -1, 1]
    direct_y = [1, -1, 0, 0]  
    queue = deque()
    queue.append((x, y))


    while queue:
        qx, qy = queue.popleft()
        visited[qx][qy] = 1
        
        #방향을 모르니 4개 다 해보자 
        for i in range(4):
            change_x = direct_x[i] + qx
            change_y = direct_y[i] + qy

            #만약에 내가 갈 다음 지점이 벽과 만난다면?
            if change_x >= n or change_y >= n or change_x <0 or change_y< 0:
                continue
            
            #만약에 내가갈 지점이 1이라면?
            if graph[change_x][change_y] == 1:
                if not graph[change_x][change_y]:
                    graph[change_x][change_y] = graph[change_x][change_y] + graph[change_x][change_y]
                    queue.append((change_x, change_y))
                    
        return graph[n - 1][n - 1]
    
print(bfs(0,0))
