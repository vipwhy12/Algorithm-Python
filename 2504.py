# 괄호의 값

# 1,‘()’ 인 괄호열의 값은 2이다.
# 2. ‘[]’ 인 괄호열의 값은 3이다.
# 3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# 4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

import sys
parenthesis = list(sys.stdin.readline().strip())

chek = [False * len(parenthesis)]

stk = []

count = 0
for i in range(len(parenthesis)):
    #괄호가 열리는 것은 항상 열어둡니다.
    if parenthesis[i] == '(' or parenthesis[i] == '[':
        stk.append(parenthesis[i])
        
    elif parenthesi[i]
    elif parenthesis[i] == ')' and stk[-1] == '(':
        count += 2
        
    elif parenthesis[i] == '[' and stk[-1] == ')' or parenthesis[i] == '[' and stk[-1] == '[':
        count += 3
        