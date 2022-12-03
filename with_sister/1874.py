# 스택 수열
# Last in First out
# 스택수열

import sys


n_arr = [];
input_arr = [];
result_arr = [];
stack = [];

answer_arr =[];

n = int(sys.stdin.readline());

#사용자 입력 arr
for _ in range(n):
  input_arr.append(int(sys.stdin.readline()));


#오름차순 배열
for i in range(1, n+1):
  n_arr.append(i);


tmep = 1;


for i in range(n):
  # 넣어주는거 false이면 멈추는데
  while( len(stack) == 0 or input_arr[i] > stack[-1] ):
    stack.append(tmep);
    answer_arr.append("+");
    #print("+");
    tmep += 1;
    
  # 빼주는거 
  while(len(stack) != 0 and input_arr[i] <= stack[-1] ): 
    a = stack.pop();
    result_arr.append(a);
    answer_arr.append("-");
    #print("-");
    

if result_arr != input_arr:
  print("NO")
else :
  for i in range(len(answer_arr)):
    print(answer_arr[i]);