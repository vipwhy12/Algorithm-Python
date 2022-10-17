
import sys

n = int(sys.stdin.readline())

#배열을 저장해주자 
fibonacci = []

#반복문을 돌아서 피보나치 리스트에 값을 저장해보자 
for i in range(n + 1):

    if i == 0:
        fibonacci.append(0)
    
    if i > 0 and i <= 2:
        fibonacci.append(1)
    
    if i > 2 and i >= 3:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        
print(fibonacci[n])