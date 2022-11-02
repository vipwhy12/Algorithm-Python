# 설탕배달 

# 상근이는 설탕가게에 N킬로그램을 배달해야함
# 설탕 공장에서 만드는 설탕은 봉지에 담겨져 있고 봉지는 3킬로그램 봉지와 5킬로 그램 봉지가 있다. 


#가장 적은 봉지의 개수를 구해보자 

# 상근이가 정확하게 N킬로그램을 배달 해야할 때 , 봉지 몇개를 가져가면 되는지 그 수를 구하는 프로그램을 작성해보자 


#정확한 N킬로 그램이 없으면 -1을 해주자 

import sys

N = int(sys.stdin.readline())

sugar = [5, 3]

dp = [0] * N

if N % 3 or N % 5 or N % 8:
    for i in sugar:
        for j in range(i, N):
            dp[j] = dp[j - i] + 1
    print(dp)
else:
    print(-1)
    