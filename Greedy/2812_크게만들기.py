import sys
input = sys.stdin.readline

n,k =map(int,input().split())
num = list(map(str,input().strip()))
delcnt = k
stack=[]

for i in range(n):
    while stack and delcnt>0 and stack[-1] < num[i] :
        stack.pop()
        delcnt -= 1
    stack.append(num[i])
for i in range(n-k) :
    print(stack[i],end='')