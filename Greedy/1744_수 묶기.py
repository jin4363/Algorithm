import sys
input = sys.stdin.readline

n = int(input())

positiveList = []
negativeList = []
oneList=[]
for _ in range(n):
    num = int(input())
    if num > 1 :
        positiveList.append(num)
    elif num <=0 :
        negativeList.append(num)
    elif num == 1 :
        oneList.append(num)
positiveList.sort(reverse=True)
negativeList.sort()
s = 0
if len(positiveList)%2==0 :
    for i in range(0,len(positiveList),2):
        s += positiveList[i] * positiveList[i+1]
else :
    for i in range(0,len(positiveList)-1,2):
        s += positiveList[i] * positiveList[i+1]
    s += positiveList[-1]
    
if len(negativeList)%2==0 :
    for i in range(0,len(negativeList),2):
        s += negativeList[i] * negativeList[i+1]
else :
    for i in range(0,len(negativeList)-1,2):
        s += negativeList[i] * negativeList[i+1]
    s += negativeList[-1]
s += sum(oneList)
print(s)