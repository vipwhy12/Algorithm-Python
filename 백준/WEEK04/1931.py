#회의실 배정

from itertools import count
from random import randrange
import sys


N = int(sys.stdin.readline())

#각 회의가 겹치치 않게 회의실을 사용할 수 있는 최대의 개수 
def meeting_room(num):
    meeting_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
    meeting_list.sort(key = lambda x: (x[1], x[0]))
    
    count = 1
    
    for i in range(len(meeting_list)):
        
        if i == 0:
            start, end = map(int, meeting_list[i])
            
        elif end <= meeting_list[i][0]:
            start = meeting_list[i][0]
            end = meeting_list[i][1]
            count += 1

    return count

print(meeting_room(N))