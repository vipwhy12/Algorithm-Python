#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.


import sys

N, M = map(int, sys.stdin.readline().split());

def dfs(depth, temp):
  if depth == M:
    print(*temp)
    return
  
  for i in range(1, N+1):
    temp.append(i)
    
    dfs(depth + 1, temp)
    temp.pop()
    
  
dfs(0, [])
#1부터 N까지 자연수 중에서 M개를 골라 
# 1부터 3까지 1 1개를 고른 수열 
#같은 수를 여러번 골라도 된다. 

#우선 하나씩 출력할 것 



#dfs 종료 조건 : 더 연결되어 있는거 있니?
#종료조건 ㅡMㅇ;니?

#인자 안에 들어[123]for문을 돌면서 1234 
#재귀특징 : 내가 가지고 있는걸 전껄로 가지고 있어 그걸 기억하고 있어 
#길이가 M인 수열을 출력하기 위해 완전탐색을 사용
#수열의 길이를 증가시키는 방향으로 문제를 풀어야 했기에 
#중복이 허용되었기에 비오름차순으로 출력 조건 


#왜 bfs와 dfs를 사용했는가 
#bfs알고리즘은 나랑 같은 레벨에 있는 애들을 먼저 탐색하겠다. 