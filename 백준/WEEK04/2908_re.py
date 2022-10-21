#외판원 순회 

import sys


N = int(sys.stdin.readline())

#city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(1<<N) for _ in range(N)]
print(dp)