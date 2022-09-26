# 수정렬하기 
# 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 수의 개수가 주어짐
#       두번째 줄에서 N개의 줄에는 수가 주어진다. 

import sys

N = int(sys.stdin.readline())

sort_list = []

for i in range(N):
    sort_list.append(int(sys.stdin.readline()))
    
sort_list.sort()

for i in range(len(sort_list)):
    print(sort_list[i])