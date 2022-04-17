import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())
graph =[[]for _ in range(N+1)]
parent =[0 for _ in range(N+1)]
for _ in range(N-1):
    nodeA, nodeB = map(int,input().strip().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)
    
def dfs(node,Pnode) :
    global parent
    parent[node] = Pnode
    if graph[node] :
        for i in graph[node]:
            if parent[i] == 0 :
                dfs(i,node)  
    else :
        return

dfs(1,1)
for i in parent[2:]:
    print(i)