# 아주 평범한 배낭 

import re
import sys


N, K = map(int, sys.stdin.readline().split())

things = []

#준서가 버틸 수 있는 모게 K
dp = [0] * (K + 1)

# 물건의 무게 / 물건의 가치 
for _ in range(N):
    things.append(list(map(int, sys.stdin.readline().split())))


def my_bag():
    for i in range(N):
        for j in range(things[i][0], K):
            if dp[j - things[i][0]] + things[i][1] > dp[j]:
                dp[j] = things[i][1] + dp[j - things[i][0]]

        
    return(dp)

print(my_bag())