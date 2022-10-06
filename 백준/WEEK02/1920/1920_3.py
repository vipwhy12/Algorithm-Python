# 수 찾기

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

#첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다. 
# 든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys

N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))

A  = int(sys.stdin.readline)
A_arr = list(map(int, sys.stdin.readline().split()))

N_arr.sort()

#인덱스 값
start = 0
end = len(N_arr)

def solution():
    center = (start + end) // 2
    
            
    
solution()

