
import sys
from tkinter import N 

solution_num = int(sys.stdin.readline())
solution_arr = sorted(list(map(int, sys.stdin.readline().split())))

def binary_search(idx, target):
    res = solution_num
    start = idx
    end = solution_num - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
            res = mid
        else:
            start = mid + 1
        
        return res
    
    
def solution():
    v1,v2 = 0, 0
    best_sum = 10 ** 10
    for i in range(N)


