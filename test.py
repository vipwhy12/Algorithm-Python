import sys

n = int(sys.stdin.readline())

def recure(n):
    if n == 0:
        return
    recure(n-1)
    print(n)
    