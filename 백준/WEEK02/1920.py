# 수찾기
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys


sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())
search_arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


search_arr.sort()

for i in arr:
    start = 0
    last = len(search_arr) -1

    while(True):
        center = (start + last) // 2 
        
        if i == search_arr[center]:
            print(1)
            break
        
        if start >= last :
            print(0)
            break

        
        elif i > search_arr[center]:
            start = center + 1
            
            
        elif i < search_arr[center]:
            
            last = center - 1
        



    
    
        