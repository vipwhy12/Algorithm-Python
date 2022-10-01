# 큐2
# 정수를 저장하는 큐를 구한 다음 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯가지이다. 
import sys 

sys.stdin = open("input.txt", "r")

num = int(sys.stdin.readline())

for _ in range(num):
    command = sys.stdin.readline()
    
    if command[0] == 'push':
        print('push')
        
    elif command[0] == 'front':
        print('front')
        
    elif command[0] == 'back':
        print('back')
        
    elif command[0] == 'pop':
        print('pop')
        
    elif command[0] == 'size':
        print('size')
        
    elif command[0] == 'empty':
        print('empty')