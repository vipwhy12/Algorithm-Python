# 스택 수열
# Last in First out

import sys
n = int(sys.stdin.readline());

n_arr = [];
input_arr = [];

#사용자가 입력하는 스택이름 : input_arr
for _ in range(n):
  input_arr.append(int(sys.stdin.readline()));

for i in range(1, n + 1):
  n_arr.append(i);

stack = [];

for i in range(n):
  if i == 0:
    for j in range(1, input_arr[0]):
      stack.append(j);
      print("+\n");
      if j == input_arr[0]: 
        stack.pop(j);
        print("-\n");
        break;  
  else :
    #내가 만약 3이야 
    
    #내가 arr안에 있으면 반복해서 빼주고 
    if input_arr[i] in stack:
      for _ in range(n):
        print("-\n")
        pop_value = stack.pop();
        if pop_value == input_arr[cnt]:
          break;
    else:
    #내가 arr안에 없으면 내가 있을 때 까지 넣어줘
      for j in range(i, input_arr[i]):
        stack.append(j);
        print("+\n");
    
  if tmp == stack[cnt]:
    print("-\n")
    stack.pop();
    tmp = stack[-1];
  



# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1