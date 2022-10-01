# A + B - 3
# 문제: 두 정수와 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에는 A와 B가 주어진다.
# 출력: 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.(0 < A, B < 10 )
import sys

repeat = int(sys.stdin.readline())

for i in range(repeat):
    a,b = map(int, sys.stdin.readline().split(" "))
    print(a + b)