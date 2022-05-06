import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split(' ')))
m = int(input())
m_list = list(map(int,input().split(' ')))
n_list.sort()
ans = []
for target in m_list:
    res = 0
    left, right = 0, n-1
    while left <= right :
        mid = (left + right) //2
        if n_list[mid] == target :
            res = 1
            break
        if n_list[mid] > target :
            right = mid - 1
        else : 
            left = mid + 1
    ans.append(res)

for i in ans :
    print(i)
        
    