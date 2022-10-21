#동전 

import sys
from unittest import result


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M + 1)
    
    #동전 총 0원을 만드는 가지수는 1이다.
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] = dp[i - coin] + dp[i]
    
    print(dp[M])