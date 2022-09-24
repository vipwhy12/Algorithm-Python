# 달팽이는 올라가고싶다.
# 문제 : 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다. 
#       달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다. 
#       달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는 지 구하는 프로그램을 작성하시오.

import sys
A, B, V = map(int, sys.stdin.readline().split())


complite_day = 0
total = 0

while True:
    total = A - B + total
    if total >= V:
        print(complite_day)
        break
    else: 
        complite_day = complite_day + 1 


#while True:
#    if a - b >= V :    
#        print(complite_day)
#        break
#    else:
#        complite_day = complite_day + 1

