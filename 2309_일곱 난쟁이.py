
data=[]
check=[]
sum=0
for i in range(9):
    inData = int(input())
    data.append(inData)
    check.append(1)
    sum += inData
data.sort()
for i in range(8):
    for j in range(1,9):
        if ( sum-(data[i] + data[j]) ) == 100:
            check[i] = 0
            check[j] = 0
            sum = 100
            break;
    if sum == 100 :
        break;
    
for i in range(9):
    if check[i] != 0:
        print(data[i])



                