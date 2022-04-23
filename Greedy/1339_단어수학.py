import sys
input = sys.stdin.readline
n = int(input())
alphabet= {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,
           'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
arr = []
valList=[]
ans=0
for _ in range(n):
    arr.append(input().strip())

for ABC in arr :
    for i in range(len(ABC)):
        num = 10** (len(ABC) - i - 1)
        alphabet[ABC[i]] +=num
        
for val in alphabet.values():
    if val > 0 :
        valList.append(val)

valList.sort(reverse=True)

for i in range(len(valList)):
    ans += valList[i] * (9-i)
    
print(ans)
