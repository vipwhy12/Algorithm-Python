#히오스 프로게이머

import sys

num, level_sum= map(int, sys.stdin.readline().split())
charactor_arr = [int(sys.stdin.readline()) for i in range(num)]

charactor_arr.sort()

#캐릭터를 정할때 
# 올라갈 것을 목표로 하는 최소목표 레벨과 최대목표 레벨을 기준으로 한다.
start = charactor_arr[0]
end = charactor_arr[0] + level_sum

while start <= end :
    center = (start + end) // 2
    total = 0
    
    
    for i in charactor_arr:
        if center > i:
            total += center - i
            
            
            
    for i in charactor_arr:
        if center > i:
            total += center - i
    
    if total <= level_sum:
        start = center + 1
        res = max(mid)
        
    
    

    
    
    
    for i in range(charactor_arr - 1):
        charactor_arr + center
