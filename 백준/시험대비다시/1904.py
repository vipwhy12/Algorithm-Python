#01타일 

import sys


n = int(sys.stdin.readline())
dp = [0] * (n

def tile_zero(num):
    for i in range(num - 1):
        if i == 0:
            dp[i] = 1
            
        if i == 1:
            dp[i] = 2
            
        if i >= 2:
            dp[i] = dp[i - 1] + dp[i - 2]
            
    return dp[-1]

print(tile_zero(n))