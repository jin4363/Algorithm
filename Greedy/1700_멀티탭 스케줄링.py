import sys
input =sys.stdin.readline

n,k = map(int,input().split())
schedule = list(map(int,input().split()))
cnt=0
plugList = []

for i in range(k):
    if schedule[i] in plugList :
        continue
    if len(plugList) < n :
        plugList.append(schedule[i])
        continue
    idxs=[]
    for j in range(n):
        try :
            idx = schedule[i:].index(plugList[j])
        except:
            idx=101
        idxs.append(idx)
    plug_out = idxs.index(max(idxs))
    print(plug_out)
    del plugList[plug_out]
    plugList.append(schedule[i])
    cnt +=1
    
            
print(cnt)

                    