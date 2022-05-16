import sys
input = sys.stdin.readline

n = int(input())
rgb_list =[]
for i in range(n):
    rgb_list.append(list(map(int,input().split(' '))))

for i in range(1,len(rgb_list)) :
    rgb_list[i][0] += min(rgb_list[i-1][1],rgb_list[i-1][2])
    rgb_list[i][1] += min(rgb_list[i-1][0],rgb_list[i-1][2])
    rgb_list[i][2] += min(rgb_list[i-1][0],rgb_list[i-1][1])

print(min(rgb_list[n-1][0],rgb_list[n-1][1],rgb_list[n-1][2]))