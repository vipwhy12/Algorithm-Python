# 사칙연산
# 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 입력 : 두 자연수 A와 B 가 주어진다.  1<= A, B <= 10000
import sys

a, b = map(int, sys.stdin.readline().split())

if 1 <= a and b <= 1000 :
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)