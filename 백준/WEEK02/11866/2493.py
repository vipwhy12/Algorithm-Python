import sys

N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))

last_valued = N_arr[0]
stk = []
arr = []

for i in range(N):
    #크거나 같다면 => 무조건 저장
    if N_arr[i] >= last_valued:    
        if len(stk) != 0 and N_arr[stk[-1] - 1] < N_arr[i] :
            stk.append(i + 1)
            arr.append(0)
        elif len(stk) != 0 and N_arr[stk[-1] - 1] >  N_arr[i]:
            arr.append(stk[-1])
        #아무것도 없으면 0    
        elif len(stk) == 0:
            arr.append(0)
            stk.append(i)
    elif N_arr[i] < last_valued:
        arr.append(i)
        
    last_valued = N_arr[i]

print(arr)