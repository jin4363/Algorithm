import sys
input = sys.stdin.readline

N, M = map(int,input().split(' '))
m_list = list(map(int,input().split(' ')))
left, right = 1,max(m_list)

while left <= right :
    res = 0
    mid = (left + right) // 2
    for tree in m_list :
        if tree - mid > 0 :
            res += tree - mid
    if res >= M :
        left = mid +1 
    else:
        right = mid - 1
print(right)