#문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별을 N개 찍는 문제
#입력 : 첫째 줄에 N(1 <= N <= 100)이 주어진다. 
import sys

star = int(sys.stdin.readline())
my_star = ''

for j in range(star):
    my_star += '*'
    print(my_star)