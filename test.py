import sys 

N, M = map(int, input().split())
tree = list(map(int, input()))
start = 0
end = max(tree)

while start <= end:
    center = (start + end) // 2
    
    depth = 0
    
    for i in tree:
        if i >= center:
            depth += (i - center)
        
    if depth >= M:
        start = center + 1
    else:
        end = center - 1