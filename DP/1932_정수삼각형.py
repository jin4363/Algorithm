import sys
input = sys.stdin.readline

trgl = []
ans = 0
n = int(input())
dp = [[0 for j in range(i+1)]  for i in range(n)]

for _ in range(n):
    trgl.append(list(map(int,input().rstrip().split(' '))))
dp[0][0] = trgl[0][0]
for i in range(1,n):
    for j in range(len(trgl[i])):
        if j==0 :
            dp[i][j] = dp[i-1][j] + trgl[i][j]
        elif j==i :
            dp[i][j] = dp[i-1][j-1] + trgl[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+trgl[i][j],dp[i-1][j]+trgl[i][j])
print(max(max(dp)))
        