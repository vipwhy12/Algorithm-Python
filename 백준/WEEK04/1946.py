# 1946 신입사원

import heapq
import queue
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    sort_score = sorted(score, key = lambda x : (x[0], x[1]))
    
    temp = sort_score[0][1]
    pass_score = 1
    
    for i in range(1, len(sort_score)):
        #봐봐 그럼 정렬한거 뒤의 것을 비교해서 나보다 크면? count해주자
        if temp <= sort_score[i][1]:
            pass_score += 1
            temp = sort_score[i][1]

    print(pass_score)