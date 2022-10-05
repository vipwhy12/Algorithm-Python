# 두 용액
import sys


N = int(sys.stdin.readline())
solution_arr = list(map(int, sys.stdin.readline().split()))

#정렬을 진행합니다. 
solution_arr.sort()

#값의 비교를 진행할 투 포인터 
#즉 리스트의 인덱스
right_pointer = N - 1
left_pointer = 0

#합이 최소가 되려면??
answer = abs(solution_arr[left_pointer] +  solution_arr[right_pointer])
final = [solution_arr[left_pointer], solution_arr[right_pointer]]

while left_pointer < right_pointer:
    
    left = solution_arr[left_pointer]
    right = solution_arr[right_pointer]
    
    sum = left + right
    
    if abs(sum) < answer :
        answer = abs(sum)
        final = [left, right]
        if answer == 0:
            break
    
    if sum < 0:
        left_pointer += 1
    else:
        right_pointer -= 1
        
print(final[0], final[1])