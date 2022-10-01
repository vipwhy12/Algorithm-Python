for i in range(len(parentheses)):
        
        if i == 0 :
            print('YES')
        
        if close_parentheses < open_parentheses:
            print('NO')
            break
        else :
            
            last_one = parentheses.pop
        
            if last_one == ')':
                close_parentheses += 1 
            elif last_one == '(':
                open_parentheses += 1 