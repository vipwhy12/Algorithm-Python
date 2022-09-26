# 소수찾기 
# 소수 찾기
# 문제: 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

#소수 리스트
minority_list = []
sosu = 0

for i in range(N):
    #만약 arr[i]가 1이 아니고,
    error = 0
    if arr[i] != 1:
        # 나누어 떨어지는게 있을 때
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                error += 1
        if error == 0: 
            sosu += 1


print(sosu)
    
