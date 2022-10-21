# 외판원 순회
import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**8)

N = int(input())
graph = []
for _ in range(N):
    graph.append(tuple(map(int, input().split(' '))))

# 1<<N == 1*2^N
dp = [[0]*(1<<N) for _ in range(N)]
print(dp)

# x: 현재 위치
# visit: 현재 위치를 포함해서 방문한 이력
def dfs(x, visit):
	# 이미 인자로 받은 visit 정보와 함께 x에 온 이력이 있는지 
    # 있다면 0(초기값)이 아닐 것 -> 최소 비용이 이미 dp에 담겨 있을 것
    # 없다면 0(초기값)일 것 -> if 조건에 맞지 않음
    if dp[x][visit]:
        return dp[x][visit]
	
    # 모든 노드를 방문했는지
    # 했다면 마지막 노드(현재 노드==x)에서 0(시작점)으로 돌아갈 방법이 있는지
    
    if visit == (1 << N)-1:
        if graph[x][0]:
            return graph[x][0]
        return sys.maxsize

	# 위의 if문들의 조건 모두 맞지 않아 여기까지 왔다는 것은
    # 인자로 주어진 visit 정보로 x라는 노드에 처음 방문했다는 의미
    # 주어진 visit을 통해 방문한 적 없는 노드가 무엇인지 알고
    # 그곳들을 방문했을 때의 최소비용을 알아내야 함
    min_cost = sys.maxsize
    for i in range(1, N):
    
    # 현재 위치(x)에서 i로 가는 방법이 없거나
    # 이미 i 노드를 방문한 이력이 visit에 담겨 있다면 
        if not graph[x][i] or visit & (1<<i):
            continue
            
        # dfs로 방문하지 않은 노드들을 방문해줘야 함
        # visit | (1<<i)로 i번째 노드까지 방문했다는 것을 표시하고
        # graph[x][i]를 더해줌으로써 x->i로 갈 때 필요한 비용을 더함
        tmp = dfs(i, visit|(1<<i))+ graph[x][i]
        
        # 최소 비용을 알고 싶기 때문에 
        # 현재 위치 x에서 방문하지 않은 노드를 방문하는 여러가지 방법들 중 최소 비용으로 min_cost를 갱신함
        if tmp < min_cost:
            min_cost = tmp
    dp[x][visit] = min_cost
    return min_cost

print(f'{dfs(0, 1)}')