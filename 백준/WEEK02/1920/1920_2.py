import sys


compare = int(sys.stdin.readline())
compare_arr = list(map(int, sys.stdin.readline().split()))

arr_num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

compare_arr.sort()

for i in range(len(arr)) :
    start = 0
    end = arr_num - 1
    
    while start <= end:
        center = (start + end) // 2
        
        if compare_arr[center] ==  arr[i]:
            print(1)
            break
        
        if compare_arr[center] >= arr[i]:
            end = center - 1
            
        else: 
            start = center + 1
    
    if start > end:
        print(0)
