# 팩토리얼
# 문제 : 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline())

def factorial(N):
    if N == 0:
        return 1
    return factorial(N-1) * N
        
print(factorial(4)) 
