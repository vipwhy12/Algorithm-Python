#미로탐색



from collections import deque
from pickle import TRUE
from re import T
import sys 

sys.stdin = open("백준/WEEK03/다시/input.txt", "r")

n, m = map(int, sys.stdin.readline().split())

nodes = []
visited_list = [[False for x in range(m)] for y in range(n)]
for _ in range(n):
    nodes.append(list(map(int, list(sys.stdin.readline().strip()))))
    
print(nodes)

count = 0

def dfs(x, y):
    direct_x = [0, 0, -1, 1]
    direct_y = [1, -1, 0, 0]  
    queue = deque()
    queue.append((x, y))
    
    #큐에 값이 없을 때 까지 
    while queue:
        test_x, test_y = queue.popleft()
        visited_list[test_x][test_y] = True
        #방향을 찾아 
        for i in range(4):
            change_x = direct_x[i] + test_x
            change_y = direct_y[i] + test_y
        
        
            if change_x >= n or change_y >= m or change_x <0 or change_y< 0:
                continue
            
            if nodes[change_x][change_y] == 1:
                if not visited_list[change_x][change_y]:
                    nodes[change_x][change_y] = nodes[test_x][test_y] + nodes[change_x][change_y]
                    queue.append((change_x, change_y))
                    print("=======")
                    print(queue)
                    print(nodes)
                
    return nodes[n - 1][m - 1]
        

        
        

print(dfs(0,0))