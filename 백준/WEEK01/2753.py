#문제 : 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오
#       윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다. 
import sys

leap_year = int(sys.stdin.readline())

if (leap_year % 4 == 0) and ((leap_year % 100 != 0) or leap_year % 400 == 0):
    print(1)
else: 
    print(0)