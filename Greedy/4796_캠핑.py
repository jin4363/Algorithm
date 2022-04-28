import sys
input = sys.stdin.readline
case=1
while True :
    canUseDay,continueDay,vacationDay = map(int,input().strip().split())
    if canUseDay == 0 and continueDay ==0 and vacationDay ==0 :
        break
    ans = 0
    while vacationDay >= 0 :
        if vacationDay - canUseDay >= 0 :
            ans += canUseDay
        else :
            ans += vacationDay
        vacationDay -= continueDay
    print('Case %d: %d'%(case,ans))
    case+=1