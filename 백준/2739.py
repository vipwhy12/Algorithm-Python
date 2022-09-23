#문제: N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 
#입력: 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

N = input()

for i in range(1,10):
    multiplication = str(int(N) * i) 
    print(N + " * " +  str(i) + " = " + multiplication)