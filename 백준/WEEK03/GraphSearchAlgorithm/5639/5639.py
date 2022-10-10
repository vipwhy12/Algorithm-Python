#이진 검색 트리
import sys 

sys.setrecursionlimit(14000)
sys.stdin = open('백준/WEEK03/GraphSearchAlgorithm/5639/5639.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write

pre = []

while True:
    try:
        pre.append(int(input().rstrip()))
    except :
        break
    
    
# 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다
# 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다. 

def solution(root_index, end):
    if root_index > end:
        return
    
    #만약 root_index가 마지막일때,
    if root_index == end:
        print(f'{pre[root_index]}\n')
        return
    
    m = binary_search(root_index + 1, end, pre[root_index])
    
    solution(root_index+1, m-1)
    solution(m, end)
    print(f'{pre[root_index]}\n')
    

def binary_search(start, end, key):
    s = start
    e = end
    
    while s < e:
        m = (s + e) // 2
        if pre[m] > key:
            e = m
        else: 
            s = m + 1
    return e if pre[e] > key else e + 1


solution(0, len(pre)- 1)
