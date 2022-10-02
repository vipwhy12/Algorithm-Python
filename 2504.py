# 괄호의 값

# 1,‘()’ 인 괄호열의 값은 2이다.
# 2. ‘[]’ 인 괄호열의 값은 3이다.
# 3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# 4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

import sys
sys.stdin = open("input.txt","r")
parenthesis = list(sys.stdin.readline().strip())
stk = []
count = 0

tmp = 0

for i in range(len(parenthesis)):
    #괄호가 열리는 것은 항상 열어둡니다.
    if parenthesis[i] == '(' or parenthesis[i] == '[':
        stk.append(parenthesis[i])
        
    elif parenthesis[i] == ')':
        if stk.pop()== '(':
            count = count + 2
            tmp += 2
        else :
            print(0)
            break        
        
        
    elif parenthesis[i] == ']':
        if stk.pop() == '[':
            count = count + 3
            tmp += 3
        else :
            print(0)
            break
    
    if i == 0:
        print(count)
        