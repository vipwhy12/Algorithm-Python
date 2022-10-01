# 골드바흐의 추측
# 문제 : 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
import sys
T = int(sys.stdin.readline())
arr = []

for i in range(T):
    arr.append(int(sys.stdin.readline().strip('\n')))

#arr.sort()
sosu = []

def is_prime(num):
    if num < 2 :
        return False
    
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
        
    return True


for i in range(T):
    a = arr[i] // 2
    b = arr[i] // 2
    
    for j in range(arr[i]):
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a = a - 1
            b = b + 1 
    
    
