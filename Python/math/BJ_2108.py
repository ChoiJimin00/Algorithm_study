import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = sorted([int(sys.stdin.readline()) for _ in range(N)])

# mean
print(round(sum(num_list)/N))

 # median
print(num_list[N//2])

# frequent value
count_list = sorted(Counter(num_list).items(), key = lambda x: (-x[1],x[0])) # sort의 기준 1.value(카운트 개수) 2.key(숫자자체)
# breakpoint()
if N==1:
    print(num_list[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

# range
print(num_list[-1]-num_list[0])