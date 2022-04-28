import sys
input = sys.stdin.readline

a,b = map(str,input().split())

bigA = ''
smallA = ''
bigB = ''
smallB = ''
for i in a :
    if i =='5' :
        bigA +='6'
        smallA +=i
    elif i=='6' :
        smallA +='5'
        bigA +=i
    else :
        bigA +=i
        smallA +=i
        
for i in b :
    if i =='5' :
        bigB +='6'
        smallB +=i
    elif i=='6' :
        smallB +='5'
        bigB +=i
    else :
        bigB +=i
        smallB +=i
print(int(smallA)+int(smallB),end=' ')
print(int(bigA)+int(bigB))