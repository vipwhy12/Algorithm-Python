import sys
sys.stdin = open("백준/WEEK02/2805/input.txt","r")

tree, M = map(int, sys.stdin.readline().split())
tree_arr = list(map(int, sys.stdin.readline().split()))

tree_arr.sort()

start = 1
end = tree_arr[-1]


while(start >= end):
    center = (start + end) // 2
    total = 0
    for i in range(tree):
        total = total + (tree_arr[i] - center)
        
    if total >= M:
        start = center + 1
    else:
        end = center - 1

print(end)
    
    
    
    