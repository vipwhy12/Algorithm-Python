# 숫자의 개수
# 문제 : 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
import sys

num = list(int(input()) for i in range(3))
multiplication = num[0] * num[1] * num[2]

list_multiplication = list(map(int, str(multiplication)))

for i in range(10):
    print(list_multiplication.count(i))