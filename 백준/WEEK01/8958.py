# X보다 작은 수 
# 문제 : "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
import sys

repeat = int(sys.stdin.readline())
for i in range(repeat) :
    answer = sys.stdin.readline()
    
    #OX 채점하기
    score = 0
    test = 0
    for j in range(len(answer)):
        if 'O' == answer[j]:
            test += 1
            score += test
        else:
            test = 0
    print(score)