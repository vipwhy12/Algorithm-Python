# 팩토리얼
# 문제 : 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

import sys
N = int(sys.stdin.readline())

def factorial(N):
    if N == 0:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄    
    return factorial(N - 1) * N   # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

print(factorial(N))
        

