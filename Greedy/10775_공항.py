import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
planes = []
parent =[i for i in range(g+1)]
for _ in range(p):
    planes.append(int(input()))
ans=0
#유니온 파인드 알고리즘
def find(x):
    if parent[x] == x :
        return x
    parent[x] = find(parent[x])
    return parent[x]

for plane in planes :
    docking = find(plane)
    if docking == 0 :
        break
    parent[docking] = parent[docking -1]
    ans += 1

print(ans)
