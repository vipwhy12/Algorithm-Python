# 색종이 만들기
import sys
from unittest import result 

sys.stdin = open("input.txt","r")

cut = int(sys.stdin.readline())
colored_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(cut)]

for i in range(len(colored_paper)):
    print(colored_paper[i])


white_paper = 0
blue_paper = 0

def solution(x, y, cut):
    #종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 
    # 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.
    color = colored_paper[x][y]
    for i in range(x, x + cut):
        for j in range(y, y + cut):
            if color != colored_paper[i][j]:
                solution(x, y, cut // 2)
                solution(x + cut // 2, y, cut // 2)
                solution(x + cut // 2, y // 2, cut // 2)
                return                
        if color == 0 :
            result.append(0)
        else :
            result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))

        
    