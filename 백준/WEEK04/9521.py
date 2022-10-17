#LCS

import sys

first_word =  '0' + sys.stdin.readline().rstrip()
secound_word = '0' +  sys.stdin.readline().rstrip()

#print(first_word,secound_word )
#print(len(first_word)) -> 6
#print(len(secound_word)) - > 6

#첫번째 단어와 두번째 단어를 비교할 행렬을 만들자
dp = [[0] * (len(first_word) + 1)] * (len(secound_word))
print(dp)

# 반복문을 돌면서 dp에 체크해주고 마지막 인덱스를 print 해주세요
for i in range(1, len(first_word)):
    for j in range(1, len(secound_word)):
        if first_word[i] == secound_word[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[-1][-1])


