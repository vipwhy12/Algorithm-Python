# 연산자 끼워넣기

import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
test = list(map(int, sys.stdin.readline().split()))

#최대 최소
mini = float('inf')
maxi = float('-inf')

def find_num(depth, num ,plus, minus, mul ,div):
    global mini
    global maxi
    
    if depth == len(arr):
        if maxi <= num:
            maxi = num
        
        if mini >= num:
            mini = num

    
    
    if plus >= 1:
        find_num(depth + 1, num + arr[depth], plus-1, minus, mul ,div)
        
    if minus:
        find_num(depth + 1, num-arr[depth], plus, minus-1, mul ,div)
        
    if mul:
        find_num(depth + 1, num * arr[depth], plus, minus, mul-1 ,div)
    
    if div:
        find_num(depth + 1, num//arr[depth],plus, minus, mul ,div-1 )
        
        
find_num(1, arr[0], test[0], test[1], test[2] ,test[3])

print(maxi)
print(mini)