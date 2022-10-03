import sys
from unittest import result


N, square_num = map(int, sys.stdin.readline().split())

arr = [[*map(int, input().split())] for _ in range(N)]

#제곱근을 반복하는 루트
def square_root(U, V):
    n = len(U)
    test = [[0] * N for _ in range(N)]
    #반복을 3번

    for row in range(N):
        for col in range(N):
            e = 0
            for i in range(N):
                e += U[row][i] * V[i][col]
            test[row][col] = e % 1000
            
    return test


def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
                
        return A
    tmp = square(A, B//2)
    
    if B % 2:
        return square_root(square_root(tmp, tmp), A)
    else:
        return square_root(tmp, tmp)

result = square(A, B)
for r in result:
    print(*r)