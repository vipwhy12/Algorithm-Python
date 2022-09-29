import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
routes =[]

for _ in range(N):
    routes.append(list(map(int, input().split(' '))))

visited_contry = [False for _ in range(N)]

minWeight = 1000000 * N

def solution(depth, total, preIdx, startNode):
    global minWeight
    # 만약 깊이가 다들어갔다면?
    if depth == N-1:
        #만약 가는길이 없지 않다면 최종 시간에 더해주세요
        if routes[preIdx][startNode]  != 0:
            total += routes[preIdx][startNode]
            minWeight = min(minWeight, total)
        return
    else:
        if total > minWeight:
            return
        
        for i in range(N):
            if visited_contry[i] == False and routes[preIdx][i] != 0:
                visited_contry[i] = True
                solution(depth + 1, total + routes[preIdx][i], i, startNode)
                visited_contry[i] = False
                
                
for i in range(N):
    visited_contry[i] = True
    solution(0,0,i,i)   
    visited_contry[i] = False
    
print(str(minWeight))