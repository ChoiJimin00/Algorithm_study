d_num = []

for num in range(1,10000):
    final = num
    str_num = str(num)
    for i in range(len(str_num)):
        final += int(str_num[i])
    d_num.append(final)
    
origin_num = set(range(1,10001,1))
output = sorted(list(origin_num - set(d_num)))

for i in output:
    print(i)