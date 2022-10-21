import sys

n  = int(sys.stdin.readline())

dp =[0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
	dp[i] = (dp[i - 2] + dp[i - 1]) % 15746


print(dp[n])


#내가 처음 작성했던 코드(메모리초과)
#n = int(sys.stdin.readline())
#dp = [0] * (n - 1)

#def tile_zero(num):
    #for i in range(num - 1):
        #if i == 0:
            #dp[i] = 1
            
        #if i == 1:
            #dp[i] = 2
            
        #if i >= 2:
            #dp[i] = dp[i - 1] + dp[i - 2]
            
    #return dp[-1]

#print(tile_zero(n))