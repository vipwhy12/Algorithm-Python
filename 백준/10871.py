# X보다 작은 수
# 문제 : 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

import sys

#첫 줄에 N과 X가 주어짐
N, X = map(int, sys.stdin.readline().split())

#A를 이루는 정수 N개가 주어짐
A = list(map(int, sys.stdin.readline().split()))

# 수열을 이루는 정수 N개가 주어짐.
arr = [num for num in A if num < X]

for i in arr:
    print(i, end=" ")





