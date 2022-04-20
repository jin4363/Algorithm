import sys
input = sys.stdin.readline


def dfs(node) :
    global data
    data[node] = -2
    for i in range(n):
        if node == data[i] :
            dfs(i)

n = int(input())
data = list(map(int,input().split()))
deleteNode = int(input())
cnt = 0

dfs(deleteNode)
for i in range(n) :
    if data[i] != -2 and i not in data:
        cnt +=1
print(cnt)
