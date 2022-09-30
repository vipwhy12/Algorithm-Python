# 나무자르기
# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고,
# 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.
import sys
from tkinter.tix import Tree

# 나무의 수 N
# 집으로 가져가려고 하는 나무의 길이 M

sys.stdin = open("input.txt","r")

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) 

while start <= end: 
    mid = (start+end) // 2
    
    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)