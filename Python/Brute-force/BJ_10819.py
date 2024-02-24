N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

sum_value = 0

if N % 2 == 0 : 
    a = abs(num_list[(N-1)//2] - num_list[-1])
    b = abs(num_list[(N-1)//2+1] - num_list[0])
    
    if a > b:
        initial = num_list[(N-1)//2]
    else:
        initial = num_list[(N-1)//2+1]
else:
    initial = num_list[(N-1)//2]

num_list.pop(num_list.index(initial))

while num_list:
    big_diff = abs(initial - num_list[0])
    idx = 0
    
    for num in num_list:
        if big_diff < abs(initial-num):
            big_diff = abs(initial-num)
            idx = num_list.index(num)
    
    sum_value += big_diff
    initial = num_list[idx]
    num_list.pop(idx)
    
print(sum_value)