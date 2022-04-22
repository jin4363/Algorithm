import sys
input = sys.stdin.readline

n =int(input())
ropes=[]
for i in range(n):
    ropes.append(int(input()))
cnt =1
ropes.sort(reverse=True)
for i in range(n):
    ropes[i] = ropes[i] * cnt
    cnt +=1  
ropes.sort(reverse=True)
print(ropes[0])