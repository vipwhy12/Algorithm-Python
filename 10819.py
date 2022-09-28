# 차이를 최대로
# N개로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 
# 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.


N = int(input());

# 수 정렬 배열
A = sorted(list(map(int,input().split())));

def fun2(arr):
    ans = 0;
    for i in range(1,len(arr)):
        # 값을 절댓값으로 바꾸고 ans 에 더해줌
        ans += abs(arr[i-1] - arr[i]);
    return ans;

r = 0;

def fun(v,c):
    global r;
    if N <= c:
        r = max(fun2(list(map(int,v.rstrip().split()))),r);
        return 

    for i in A:
        if v.count(str(i)) == 0:
            t = v + str(i) + " ";  
            fun(t,c+1);

fun('',0);

print(r);
