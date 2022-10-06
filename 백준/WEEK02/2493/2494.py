from inspect import stack
import sys 

n= int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))

stk = []
goto = [0] * n

for i in range(n):
    t = tower[i]
    while stk and tower[stk[-1]] < t:
        stack.pop()
    if stack:
        goto[i] = stk[-1] + 1
        
    stk.append()
    
print()