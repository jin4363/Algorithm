
T = int(input())
for tt in range(T):
    n = int(input())
    bi_str = bin(n).split('0b')
    n_to_bi = str(bi_str[1])
    a = n_to_bi[::-1]
    idx = 0
    result =[]
    for i in a :
        if i == '1':
            result.append(idx)
        idx += 1
    for i in result :
        print(i,end=' ')

