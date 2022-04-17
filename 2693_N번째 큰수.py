lineNum = int(input())

for lineNum in range(0,lineNum):
    numList = list(map(int,input().split()))
    numList.sort(reverse=True)
    print(numList[2])