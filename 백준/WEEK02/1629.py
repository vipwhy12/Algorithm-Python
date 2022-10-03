# 곱셈
# 자연수 A를 B번 곱한 수를 알고 싶다. 
# 단 구하려는 수가 매우 커질 수 있으므로 

import sys


A, B, C = map(int, sys.stdin.readline().split())


#base_case : A ** B % 12

def totalidad(A, B, C):
    #재귀함수가 바닥을 찍었을 때,
    if B == 1:
        return A % C
    
    test = B % 2
    
    if test == 0:
        return (totalidad(A, B//2, C) % C) ** 2

    elif test == 1:
        return (A * (totalidad(A, B//2 , C) % C) ** 2) % C

print(totalidad(A, B, C))