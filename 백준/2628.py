# 종이자르기
# 문제 : 아래 <그림 1>과 같이 직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.

import sys
import this

#sys.stdin = open("input.txt","r")
#가로, 세로
width, height = map(int, sys.stdin.readline().split())

#자를 가로 값
cut_width = []

#자를 세로값
cut_height = []

for i in range(int(input())):
    cut = list(map(str, sys.stdin.readline().split()))
    if(int(cut[0]) == 0):
        cut_width.append(int(cut[1]))
    elif(int(cut[0]) == 1):
        cut_height.append(int(cut[1]))

#꼭지점의 시작점
#cut_width.append(0)
#cut_height.append(0)

cut_width.append(height)
cut_height.append(width)

cut_width.sort()
cut_height.sort()

max_width = 0 
max_height = 0

for i in range(1, len(cut_width)):
    gap = cut_width[i] - cut_width[i - 1]
    if max_width < gap:
        max_width = gap
        
for i in range(1, len(cut_height)):
    gap = cut_height[i] - cut_height[i - 1]
    if max_height < gap:
        max_height = gap

print(max_width * max_height)