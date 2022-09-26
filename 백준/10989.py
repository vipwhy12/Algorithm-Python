# 수 정렬하기3
# 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())
    
print(arr.sort())