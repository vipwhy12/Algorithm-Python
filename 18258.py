# 큐2
# 정수를 저장하는 큐를 구한 다음 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯가지이다. 
import sys
from xml.etree.ElementTree import Comment 

sys.stdin = open("input.txt", "r")

num = int(sys.stdin.readline())

q = [0] *  2000000
count = 0

for _ in range(num):
    command = sys.stdin.readline().split()
    #order = command[0]
    
    if command[0] == 'push':
        q[count] = command[1]
        count += 1  

    elif command[0] == 'front':
        if q[0] == 0:
            print(-1)
        else :
            print(q[0])
            
    elif command[0] == 'back':
        if q[0] == 0:
            print(-1)
        else :
            print(q[count - 1])
        
    elif command[0] == 'pop':
        if q[0] == 0:
            print(-1)
        else :
            print(q[0])
            del q[0]
            #q = q[1:-1]
            count -= 1
    
            #q.remove(q[0])
            #q.pop(0) 
            #del q[0]
        
    elif command[0] == 'size':
        print(count)
        
    elif command[0] == 'empty':
        if q[0] == 0:
            print(1)
        else:
            print(0)
            count = 0