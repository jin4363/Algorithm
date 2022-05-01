import sys
input = sys.stdin.readline

name=list(map(str,input().strip()))
name.sort()
leftIdx = 0
rightIdx = len(name) - 1
last=[]
ans=['?']*len(name)
while name :
    if name.count(name[0]) >= 2:
        ans[leftIdx] = name.pop(0)
        ans[rightIdx] = name.pop(0)
        leftIdx +=1
        rightIdx -= 1
    else :
        last.append(name.pop(0))
        
if len(last) >= 2 :
    print('I\'m Sorry Hansoo')
else :
    if last :
        ans[ans.index('?')] = last[0]
    for i in ans :
        print(i,end='')
    
