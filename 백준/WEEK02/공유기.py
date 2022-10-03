import sys 

house, router = map(int, sys.stdin.readline().strip().split())
house_arr = [int(sys.stdin.readline().strip()) for i in range(house)]

house_arr.sort()

#거리를 이진탐색으로 최대거리를 찾아보자 
start = 1
end = house_arr[-1] - house_arr[0]

while(True):
    #공유기를 설치할 수 있는 최대거리 설정
    center = (start + end) // 2
    count = 0
    router_check = house_arr[0]
    
    #집을 돌면서 라우터를 설치할 수 있는지 확인합니다. 
    for i in house_arr:
        if i - router_check <= center:
            count += 1
            router_check = i
            print("설치되었습니다.")
        
    # 만약 집에 설치될 라우터 개수보다 부족하다면?
    if count >= router:
        result = center
        start = center + 1
    # 만약 집에 설치될 라우터 개수 보다 많더면?
    else :
    



