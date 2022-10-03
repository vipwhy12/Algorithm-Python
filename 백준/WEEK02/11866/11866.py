import sys 

N, k = map(int, sys.stdin.readline().split())
yosefuse_arr = [i for i in range(1, N + 1)]
kill_log = []

count = 1

while(len(yosefuse_arr) >= 1):
    remove_value = 0
    y_len = len(yosefuse_arr)
    
    if len(yosefuse_arr) == 1:
        kill_log.append(yosefuse_arr[0])
        break
        
        
    for i in range(y_len):
        if count == k:
            kill_log.append(yosefuse_arr[ i - remove_value])
            del yosefuse_arr[i - remove_value]
            count = 1
            remove_value += 1
        else :
            count += 1
    

        
print('<'+ ', '.join(f'{x}' for x in kill_log ) + '>')