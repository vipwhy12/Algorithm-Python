#LCS

import sys


first_word = list(sys.stdin.readline().strip())
second_word = list(sys.stdin.readline().strip())

dp = [0] * len(second_word)

for i in range(len(first_word)):
    count = 0 
    for j in range(len(second_word)):
        if count < dp[j]:
            count = dp[j]
        #만약 나랑 같은 걸 만났어! 그럼 + 1을 해줘
        if first_word[i] == second_word[j] : 
            dp[i][j] = count + 1
        
        

