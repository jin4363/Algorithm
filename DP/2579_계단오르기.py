import sys
input = sys.stdin.readline
n =int(input())
st = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(n) :
    st[i] = int(input())
dp[0] = st[0]
dp[1] = st[0] + st[1]
dp[2] = max(st[1] + st[2], st[0] + st[2])
for i in range(3,n):
   dp[i] = max(dp[i-3] + st[i-1] + st[i],dp[i-2] + st[i] )

print(dp[n-1])