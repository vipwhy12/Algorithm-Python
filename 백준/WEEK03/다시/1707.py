import sys
from collections import deque

def is_bipartite_graph(start):
    global V
    
    flag = 1
    visited[start] = flag
    queue = deque([start])

    while queue:
        size = len(queue)
        flag = -1 * flag
        
        for _ in range(size):
            cur = queue.popleft()
            
            for next in edges[cur]:
                if visited[next] == 0:
                    visited[next] = flag
                    queue.append(next)
                    
                elif visited[next] != flag:
                    return False
    return True

testcase = int(sys.stdin.readline().rstrip())

for _ in range(testcase):
    V, E = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        v, u = map(int, sys.stdin.readline().split())
        edges[v].append(u)
        edges[u].append(v)

    visited = [0] * (V+1)

    for i in range(1, V+1):
        if visited[i] == 0:
            if is_bipartite_graph(i) is False:
                sys.stdout.write('NO\n')
                break
    else:
        sys.stdout.write('YES\n')