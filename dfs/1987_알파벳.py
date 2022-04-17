import sys

input = sys.stdin.readline

R , C = map(int,input().strip().split()) 

graph = []
visited=[[0 for _ in range(C)]for _ in range(R)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(R):
    graph.append(list(input().strip()))

maxResult =0
movedList =set()

def dfs(x,y,depth) :
    global maxResult,movedList
    maxResult = max(depth,maxResult)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if not graph[nx][ny] in movedList:
                movedList.add(graph[nx][ny])
                dfs(nx,ny,depth+1)
                movedList.remove(graph[nx][ny])
    
movedList.add(graph[0][0])
dfs(0,0,1)
print(maxResult)