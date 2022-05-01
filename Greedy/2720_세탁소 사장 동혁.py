import sys
input = sys.stdin.readline

t = int(input())
ans=[]
for _ in range(t):
    qt = 0
    dime = 0
    nk = 0
    penny = 0
    m = int(input())
    if m >= 25 :
        qt = m//25
        m %= 25
    if m >= 10 :
        dime = m//10
        m %= 10
    if m >=5 :
        nk = m//5
        m %= 5
    if m >=1 :
        penny = m //1
    ans.append([qt,dime,nk,penny])
    
for i in ans:
    for j in i :
        print(j,end=' ')
    print()
        
