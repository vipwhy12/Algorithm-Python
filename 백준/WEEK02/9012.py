import sys

N = int(sys.stdin.readline())

for i in range(N):
    parenthesis = list(sys.stdin.readline().strip())
    
    stk = []
    count = 0
    
    for j in range(len(parenthesis)):
        if parenthesis[j] == '(':
            stk.append(parenthesis[j])

        elif parenthesis[j] == ')':
            if len(stk) != 0:
                del stk[-1]
            else :
                stk.append(parenthesis[j])
                break
    
    if len(stk) == 0:
        print('YES')
    else :
        print('NO')