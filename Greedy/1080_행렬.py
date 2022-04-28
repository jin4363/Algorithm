import sys
input = sys.stdin.readline


def trans(i,j):
    global beforeArr
    for x in range(i,i+3):
        for y in range(j,j+3):
            beforeArr[x][y] = 1 - beforeArr[x][y] 

beforeArr = []
afterArr = []
n,m = map(int,input().strip().split())
for i in range(n):
    beforeArr.append(list(map(int,input().strip())))
    
for i in range(n):
    afterArr.append(list(map(int,input().strip())))
cnt=0
flag=0
for i in range(n-2):
    for j in range(m-2):
        if beforeArr[i][j] != afterArr[i][j]:
            trans(i,j)
            cnt +=1

for i in range(n):
    for j in range(m):
        if beforeArr[i][j] != afterArr[i][j] :
            flag = 1
            break
if flag == 1 :
    print(-1)
else:
    print(cnt)