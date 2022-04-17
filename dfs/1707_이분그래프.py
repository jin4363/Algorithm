import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node,group) :
    if graph[node] :
        for i in graph[node] :
            if visited[i] == 0 :
                visited[i] = group * (-1)
                if not dfs(i,visited[i]) :
                    return False
            else :
                if group == visited[i] :
                    return False
    return True

t = int(input().strip())
graph=[]
visited = []
for _ in range(t):
    v,e = map(int,input().strip().split())
    graph = [[]for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for i in range(e):
        A,B = map(int,input().split())
        graph[A].append(B)
        graph[B].append(A)
    for i in range(1,v+1):
        if visited[i] == 0 :
            visited[i]=1
            res = dfs(i,1)
            if not res :
                print('NO')
                break
    if res :
        print('YES')
    
        