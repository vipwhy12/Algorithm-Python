#가장 긴 증가하는 부분 수열 


import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))


def increased(num, increased_list):
    #result = increased_list[0]
    
    dp = [1] * num
    
    for i in range(1, num):
        for j in range(i):
            if increased_list[j] < increased_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)
            
    return(max(dp))

print(increased(n, a))
