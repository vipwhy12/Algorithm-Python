# 차이를 최대로
# N개로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 
# 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
import itertools
import sys
from itertools import permutations

N = int(sys.stdin.readline())

print(N)
a = list(map(int, sys.stdin.readline().split()))

list_a = list(itertools.permutations(a))


sum_list = []

for i in range(len(list_a)):
    sum = 0
    for j in range(len(a) - 1):
        sum += abs(list_a[i][j] - list_a[i][j+1])
        sum_list.append(sum)

print(max(sum_list))