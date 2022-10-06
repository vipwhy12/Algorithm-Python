
#왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래

import sys
from unittest import result


N = int(sys.stdin.readline())

arr = []
result = []


for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

def qud_tree(x, y, N):
    screen = arr[x][y]
    
    for i in range(x, x+N):
        for j in range(y, y+N):
            if screen != arr[i][j]:
                qud_tree(x, y, N//2)
                qud_tree(x, y + N//2, N//2)
                qud_tree(x + N//2, y, N//2)
                qud_tree(x + N//2, y + N // 2, N//2)
                return
            


    if screen == 0:        
        result.append(0)
    else:
        result.append(1)
        
qud_tree(0, 0, N)
print(result)