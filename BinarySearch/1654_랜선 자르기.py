import sys
input = sys.stdin.readline

K,N = map(int,input().split(' '))
lan_list = []
for _ in range(K):
    lan_list.append(int(input()))
left,right = 1,max(lan_list)
ans = 0
while left <= right :
    mid = (left + right) // 2
    cnt = 0
    for i in lan_list :
        if i >= mid :
            cnt += i//mid
    if cnt >= N :
        #자른갯수가 더 많을 경우 자를 길이 늘려서 더 적게 잘리게 함 
        left = mid +1
    elif cnt < N : 
        #자른갯수가 더 적을 경우 자를 길이를 줄여서 더 많이 잘리게함 
        right = mid -1
        
print(right)
    