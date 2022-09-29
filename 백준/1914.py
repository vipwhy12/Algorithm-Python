import sys
n = int(sys.stdin.readline())

def hanoiTower(fisrt, second, third, count):
    if count >= 1:
        hanoiTower(fisrt, third, second, count - 1 )
        print(fisrt, third)
        hanoiTower(second, fisrt, third, count - 1 )

print(2 ** n - 1)

if n <= 20:
    hanoiTower(1, 2, 3, n)