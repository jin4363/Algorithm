import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())
A,B = map(int,input().strip().split())
T = int(input())
graph = [[]for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for i in range(T):
    P,C = map(int,input().strip().split())
    graph[P].append(C)
    graph[C].append(P)
ans = 0
def dfs(Node,depth):
    global ans,B
    if visited[B] :
        ans =  depth
        return 
    if graph[Node] :
        for i in graph[Node] :
            if not visited[i] :
                visited[i] = True
                dfs(i,depth+1)
                if visited[B] :
                    return 
visited[A] = True
dfs(A,1)
print(ans-1)