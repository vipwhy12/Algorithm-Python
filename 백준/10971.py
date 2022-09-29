#외판원 순회

from gettext import find
import sys

sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline())

maps = []
test = []

for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
    test.append([False for _ in range(N)])

total_time = []
contry = [False for _ in range(N)]



def solution(depth, time, c):
        #도착했을때(1나라부터 N 나라까지 다 들렀을때!)
    if depth == N:
        total_time.append(time)
        return 
    for i in range(N):
        for j in range(1, N):
            #만약 지도의 인덱스가 0이 아니고, 들렀던 나라가 아니라면
            if maps[i][j] != 0 and contry[c] == False and i != c and test[i][j] == False:
                # 지도에 나 표시해주세요 나 들렀어요 
                contry[c] = True
                test[i][j] = True
                solution(depth + 1, time + int(maps[i][j]), c) 
                contry[c] = False
                test[i][j] = False


for i in range(N):
    visited[i] = 1
    solution(0,0,i,i)
    visited[i] = 0
    
solution(0, 0, 0)
print(total_time)
