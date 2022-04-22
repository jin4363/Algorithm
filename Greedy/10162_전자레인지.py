import sys
input = sys.stdin.readline

t = int(input())
A, B, C = 300, 60, 10
ansA,ansB,ansC =0 ,0 ,0
if (t % C) > 0 :
    print(-1)
else :
    if t >= A :
        ansA = t//A 
        t %= A
    if t >= B :
        ansB = t//B
        t %= B
    if t >= C:
        ansC = t//C
        t %= C
    print('%d %d %d'%(ansA,ansB,ansC))
    
        