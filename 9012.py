# 괄호
# 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)

import sys 
#sys.stdin = open("input.txt","r")
count = int(sys.stdin.readline())

for i in range(count):
    
    parentheses = list(str(sys.stdin.readline().strip()))

    total = 0 
    
    for j in parentheses:
        if j == '(' :
            total += 1
            
            
        elif j == ')':
            total -= 1
            
            
        if total < 0:
            print('NO')
            break
        
    if total >  0:
        print('NO')
    elif total == 0:
        print('YES')