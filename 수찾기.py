from re import L
import sys

comparison_num = int(sys.stdin.readline())
comparison_arr = list(map(int, sys.stdin.readline().split()))

num = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))

comparison_arr.sort()
num_arr.sort()

for i in range(len(num_arr)):
    a = num_arr[i]
    
    start = 0
    end = len(comparison_arr) - 1
    
    while start <= end:
        center = (start + end) // 2
        
        if a == comparison_arr[center]:
            print(1)
            break
        
        if a < comparison_arr[center]:
            end = center - 1 
            
        elif a > comparison_arr[center]:
            start = center + 1
            
    if start >= end:
        print(0)

    
    
    