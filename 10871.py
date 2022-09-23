# X보다 작은 수
# 문제 : 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
import sys

N, X = map(int, input().split())
print(int(N))


min_list = []
for i in range(N - 1):
    min_list.append(input())

test = ""

#for i in range(len(min_list())):
#    if list[i] < X:
#        min_list.append(list[i])
#        test = test + list[i] + " " 

#print(test)
