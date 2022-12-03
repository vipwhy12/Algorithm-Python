# 출석체크

# 1. 학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다.
# 2. 본인의 입장번호의 배수의 학생들에게 보냄
# 3. K명은 졸고 있음 그래서 못보냄 ;

# Q : 지환이가 출석 코드를 보낼 학생의 수 
# N : 학생의 수  
# K : 졸고 있는 학생의 수 

# 두번째 줄에는 졸고 있는 학생의 입장 번호
# 세번째 줄에는 Q명의 출석 코드를 받을 학생의 입장번호
# 네번째 줄부터 M 개의 줄 동안 구간 범위 S, E가 공백 사이에 두고 주어짐.

import sys


N, K, Q, M = map(int, sys.stdin.readline().split());

sleep_entry = [];

for _ in range(K):
  sleep_entry.append(int(sys.stdin.readline()));

for _ in range():
  

random_entry = [];

for _ in range(Q):
  random_entry.append(int(sys.stdin.readline()));

print(random_entry);