#N과 M(4)

#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

#1부터 N까지의 자연수 중에 M개를 고른 수열 

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

def dfs(depth, temp):
  if depth == M:
    print(*temp)
    return
  
  for i in range(1, N+1):
    temp.append(i)
    dfs(depth+1, temp)
    temp.pop()

dfs(0, arr)
