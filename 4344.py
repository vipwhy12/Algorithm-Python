# 평균은 넘겠지
# 문제 : 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 소식을 알려줘야 한다. 
# 입력 : 첫째 줄에는 테스트 케이스 개수 C가 주어진다. 둘째 줄부터 각 케이스마다 학생의 수 N(1 <= N <= 1000, N은 정수)
import sys

repeat = int(sys.stdin.readline())

for i in range(repeat) :
    score = list(map(int(), sys.stdin.readline().split(" ")))
    average = 0
    for j in range(1, score[0]):
        average += j
    #for j in range(int(sys.stdin.readline())):
    #score = list(int(sys.stdin.readline()) for j in range(int(sys.stdin.readline())))
    print(average /score[0])