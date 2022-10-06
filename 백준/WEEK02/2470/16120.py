# PPAP
from inspect import stack
import sys

stack = []
is_ppap = []
word = sys.stdin.readline()


#만약 p로 시작하지 않는다면 ppap아님
if word == 'P' or word == "PPAP":
    print('PPAP')
else:
    for i in word:
        stack.append(i)
        
        # 스택 리스트 뒤에서 4번째 문자가 ['p', 'p', 'a', 'p']일 경우 
        stack.pop()
        stack.pop()
        stack.pop()
    
    #스택 리스트에 ["p", '\n']이 있으면 모든 ppap를 p로 바꿔준 것으로 ppap 출력
    
    if stack == ['p', '\n']:
        print("ppap")
    else:
        print("NP")
        
        
        #만약 p가 있으면 무조건stak에 저장하고
        if word[i] == 'P':
            stk.append(i)
        
        #만약 문자열이 A일 때
        elif word[i] == 'A' :
            
            #문자열이 A이면서 길이가 0이면 아님.
            if len(stk) <= 1:
                print('NP')
                break
            
            #만약 스택에 pp/pppp가 들어가 있다면?
            # ppap pap? p를 ppap로 바꾸었을때 
            
            elif len(stk) >= 2:
                fist_word = stk.pop()
                secound_word = stk.pop()
                
                
                if i < len(word) and word[i+1] == 'P':
                    is_ppap.append(fist_word)    
                    is_ppap.append(secound_word)    
                    is_ppap.append(word[i])
                    is_ppap.append(word[i]+1)
                    
                    print('PPAP')
                    break
                else:
                    print('NP')
                    break
                
        