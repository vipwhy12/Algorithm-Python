# 수찾기
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.


from calendar import c
import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())
arr_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))
    
arr_M.sort()
arr_N.sort()


# 기준 리스트는  M 
# 비교 리스트는 N

while(True):
    #가운데 인덱스를 자름
    center = len(arr_N) // 2
    
    for i in range(arr_M):
        if arr_M[i] == arr_N[center]:
            
    
    # 1 3 7 9
    #5 
    # 4 1 3 7 9 5
    
    
    #1. 레인지의 반을 잘라줍니다. 
    #2. 자른 반의 

# 전체를 반복할 반복문 M
for i in range(len(arr_M)):
    #리스트 M의 길이를 잘라주세요 
    for j in range(len(arr_N)):
        if arr_N[len(arr_M) // 2] < arr_M[i]:
            for j in range(arr_N):
            
            
