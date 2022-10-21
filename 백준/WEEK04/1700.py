import sys

N, K = map(int, sys.stdin.readline().split())

powerstrip_list = list(map(int, sys.stdin.readline().split()))

def min_powerstrip():
    #k만큼 만든 다음에!
    plug_list = [0] * K
    
    for i in range(K):
        plug_list[i] = powerstrip_list[i] 
    
    count = 0

    for i in range(K, len(powerstrip_list)):
        for plug in plug_list:
            if plug == 0:
                plug.append(powerstrip)
            
            #만약 00과 같지 않아 
            if plug != powerstrip:
                
    
    
    
min_powerstrip()