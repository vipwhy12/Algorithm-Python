# 평균은 넘겠지
# 문제 : 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 소식을 알려줘야 한다. 
# 입력 : 첫째 줄에는 테스트 케이스 개수 C가 주어진다. 둘째 줄부터 각 케이스마다 학생의 수 N(1 <= N <= 1000, N은 정수)
import sys

#반복할 횟수 입력
repeat = int(sys.stdin.readline())

for i in range(repeat) :
    #점수 리스트 생성
    count = 0
    temp = 0
    score = list(map(int, input().split(" ")))

    #학생들의 평균을 구하기
    for j in range(1, score[0] + 1):
        temp += score[j]
    
        
    average = temp // score[0]
    
    
    # 만약 평균 보다 크다면 
    for j in range(1, score[0] + 1):
        if average < score[j]:
            count += 1
            
    print(("{:.3f}".format(count / score[0] * 100)) + "%")