import bisect
import sys 
input = sys.stdin.readline
n= int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]

#처음부터 다시 작은수 찾는 dp 방법은 시간초과
for i in range(n):
    if arr[i] > dp[-1] :
        dp.append(arr[i])
    else :
        #biset_lfet 함수는 검색하는 수가 있으면
        #그 수의 인덱스반환, 없으면 들어갈 곳 반환
        #left 이면 4보다 큰 수의 lfet 인덱스 반환 
        idx = bisect.bisect_left(dp,arr[i])
        dp[idx] = arr[i]
print(len(dp))