# 소수찾기 
# 소수 찾기
# 문제: 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

for num in arr:
    if(num == 1):
        arr.remove(num)
    elif(num % 2 == 0 and num != 2):
        arr.remove(num)
    elif(num % 3 == 0 and num != 3):
        arr.remove(num)
    elif(num % 5 == 0 and num != 5):
        arr.remove(num)
    elif(num % 7 == 0 and num != 7):
        arr.remove(num)
    elif(num % 11 == 0 and num != 11):
        arr.remove(num)

print(arr)