
answer=0
numCount = int(input())
numList = list(map(int,input().split()))
numList.sort(reverse=True)
bigNumber = numList[0]
checkArray = [False,False] +[True]*(bigNumber-1)
for i in range(2,bigNumber+1):
    if checkArray[i] :
        for j in range(2*i,bigNumber+1,i):
            checkArray[j]=False
            
for i in range(numCount):
    if checkArray[numList[i]] == True:
        answer = answer+1
print(answer)