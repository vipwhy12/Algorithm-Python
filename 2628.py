# 종이자르기
# 문제 : 아래 <그림 1>과 같이 직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.

import sys
import this
#가로, 세로
width, height = map(int, sys.stdin.readline().split())

#자를 가로 값
cut_width = []

#자를 세로값
cut_height = []

#입력 값을 각 가로값과 세로값에 저장하자
for i in range(int(input())):
    cut = list(map(str, sys.stdin.readline().split()))
    if(int(cut[0]) == 0):
        cut_width.append(cut[1])
    elif(int(cut[0]) == 1):
        cut_height.append(cut[1])
        
cut_width.sort()
cut_height.sort()

test = []


for i in range(len(cut_width) - 1):
    if i == 0:
        width = width - int(cut_width[i])
        test.append(width)
    else :
        width = width - (int(cut_width[i]) - int(cut_width[i -1]))
        test.append(str(width))

#test.append(width)
# 가로세로 다 곱해서 가장 큰값 저장 후 출력하기
#for i in range():
#    for j in range():
print("==================")
print(test)