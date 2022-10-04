# 나무자르기

import sys
# 나무 절단기에서 중요한 부분
# 이분탐색을 진행하며 처음과 끝을 어떻게 지정할 것인가.

# 나무의 평균 거리가 아닌 최대로 자를 수 있는 나무의 길이를 구하는 것이니
# 최대 나무 길이를 start, end, center로 지정합니다.

tree_num, sangen_tree = map(int, sys.stdin.readline().split())
tree_arr = list(map(int, sys.stdin.readline().split()))

#이진탐색을 위한 리스트 정렬

start, end = 1, max(tree_arr)

while start <= end:
    total  = 0
    center = (start + end) // 2
    
    #상근이가 자를 나무
    for tree in tree_arr:
        if tree >= center:
            total += tree - center
    
    #상근이가 자른 나무를 이분탐색
    if total >= sangen_tree:
        start = center + 1
    else :
        end = center -1 

#절단기에 설정할 수 있는 높이의 최댓값을 출력
print(end)