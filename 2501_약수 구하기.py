data = input().split()

N = int(data[0])
K = int(data[1])
result_arr = []

for i in range(1,N+1) :
    if N % i ==0 :
        result_arr.append(i)


if len(result_arr) < K :
    print(0)
elif len(result_arr) > K :
    print(result_arr[K-1])
elif len(result_arr) == K :
    print(result_arr[K-1])
