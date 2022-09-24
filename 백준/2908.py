# 상수
# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

from multiprocessing.connection import answer_challenge
import sys

list_sangen = list(sys.stdin.readline().split())
answer = ''

fist_num = list_sangen[0]
second_num = list_sangen[1]

for i in range(2, -1, -1):
    answer = answer + fist_num[i]
    
fist_answer = answer
answer = ''

for i in range(2, -1, -1):
    answer = answer + second_num[i]
    
second_answer = answer
answer = ''

if fist_answer < second_answer:
    print(second_answer)
else:
    print(fist_answer)
    