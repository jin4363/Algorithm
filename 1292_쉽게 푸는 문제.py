
answer=0
startNumber, endNumber = map(int,input().split())
numberArray = []
saveNumber = 1
for i in range(1,endNumber+1):
    for j in range(1,i+1):
        if len(numberArray)<endNumber :
            numberArray.append(int(saveNumber))
    saveNumber = saveNumber + 1
    
for i in range(startNumber-1,endNumber):
    answer = answer + numberArray[i]
print(answer)