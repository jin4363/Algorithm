in_str = input()
in_list=in_str.split(' ')
num1 = int(in_list[0])
num2 = int(in_list[1])

commonDiv=0
commonMul=0

num1_arr = []
num2_arr = []

for i in range(1,num1+1):
    if i % num1 == 0:
        num1_arr.append(i)
    