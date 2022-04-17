


inPeople=[]
outPeople=[]
for i in range(10):
    inputNumber=input()
    inputNumber=inputNumber.split(' ')
    outPeople.append(int(inputNumber[0]))
    inPeople.append(int(inputNumber[1]))

nowPeople=0
nowarr=[]
bestNumber = 0
for i in range(10):
    nowPeople = (nowPeople + inPeople[i]) - outPeople[i]
    if bestNumber <= nowPeople :
        bestNumber = nowPeople
print(bestNumber)