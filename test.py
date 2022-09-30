import sys
sys.stdin = open("input.txt","r")
house, router = map(int, sys.stdin.readline().split())
location_arr = [int(sys.stdin.readline()) for _ in range(house)]

location_arr.sort()
start = 1
last = location_arr[-1] - location_arr[0]

result = 0

if router == 2:
    print(location_arr[-1] - location_arr[0])
else:
    while(start < last):
        mid = (start + last) // 2
        
        count = 1
        ts = location_arr[0]
        
        for i in range(house):
            if location_arr[i] - ts >= mid:
                count += 1
                ts = location_arr[i]        
                    
        if count >= router:
            result = mid
            start = mid + 1
        elif count < router:
            end = mid
            
    print(result)