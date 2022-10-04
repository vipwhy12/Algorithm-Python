# 공유기 설치

import imp


import sys
N, C = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for i in range(N)]

arr.sort()

start = 1
end = arr[-1] - 1

while start <= end :
    center = (start + end) // 2
    
    total = 0
    
    for i in arr:
        i = 
        total = arr[i]