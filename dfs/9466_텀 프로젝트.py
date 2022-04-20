import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
T = int(input())


def dfs(node):
    global res
    visited[node] = 1
    cycleCheck.append(node)
    nextNode = graph[node]
    
    if visited[nextNode] == 1 :
        if nextNode in cycleCheck :
            res += cycleCheck[cycleCheck.index(nextNode):]
            return 
    else :
        dfs(graph[node])
        

for _ in range(T):
    res=[]
    cnt = 0
    graph =[0]
    n = int(input())
    graph.extend(list(map(int,input().strip().split())))
    visited =[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if visited[i] == 0 :
            cycleCheck=[]
            dfs(i)
    print(n - len(res))
    
    
