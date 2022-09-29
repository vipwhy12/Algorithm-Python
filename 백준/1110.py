# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

from re import T
import sys

N = sys.stdin.readline()
arr = []
count = 0

if int(N) < 10:
    arr.append('0')
    arr.append(N[0])
else:
    arr.append(N[0])
    arr.append(N[1])


while(True):
    total = int(arr[0]) + int(arr[1])

    tmp = arr[1]
    
    arr.clear()
    arr.append(tmp)
    arr.append(str(total)[-1])

    total = int(arr[0] + arr[1])
    count += 1
    
    if total == int(N):
        print(count)
        break


    