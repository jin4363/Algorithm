import sys
input = sys.stdin.readline
dp=[0,1,2]
n=int(input())
for i in range(3,1001):
    dp.append(dp[i-2] + dp[i-1])
print(dp[n]%10007)