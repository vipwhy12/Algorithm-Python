# 제로

import sys

k = int(sys.stdin.readline())
arr = []

for _ in range(k):
    jungsu = int(sys.stdin.readline())
    
    if jungsu == 0:
        del arr[-1]
    else :
        arr.append(jungsu)
        
print(sum(arr))