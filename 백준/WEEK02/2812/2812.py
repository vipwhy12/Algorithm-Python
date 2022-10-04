import sys
sys.stdin = open("백준/WEEK02/2812/input.txt","r")


N, K = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline())

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort(reverse = True)
for i in range(K):
    arr.pop()

print(int(''.join(map(str,arr))))

