# 하노이의 어찌구 
#문제 : 첫째 줄에 옮긴 횟수 K를 출력한다. 

import sys

num_disks = int(sys.stdin.readline())




#가장 큰 원판을 제외하고 나머지원판을 start_peg에서 other_peg로 이동
#가장 큰 원판을 start_peg에서 end_peg로 이동
#나머지 원판들은 other_peg에서 end_peg로 이동?


def hanoi(num_disks, start_page, end_page):
    #원판이 하나도 없을 때,
    if num_disks == 1:
        print(start_page, end_page)
        return
    
    hanoi(num_disks - 1, start_page, 6 - end_page)
    print(start_page, end_page)
    hanoi(num_disks - 1, 6 - start_page, end_page)

print(2 ** num_disks - 1)
hanoi(num_disks, 1, 3)