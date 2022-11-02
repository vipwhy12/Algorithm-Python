#피보나치 수 2

import sys


n = int(sys.stdin.readline())
dp = [0] * (n + 1)

def fibonacci(num):
    
    
    for i in range(num + 1):
        #만약 숫자가 0일 때
        if i == 0 :
            dp[0] = 0
        
        if i > 0 and i <= 2:
            dp[i] = 1
        
        if i >= 3:
            dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[-1]

print(fibonacci(n))