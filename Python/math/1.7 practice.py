# convert to decimal
import math

base = int(input('몇 진수 인가? '))
number = input('숫자 입력: ')

num_list = []
for i in number:
    num_list.append(i)

cnt,num = 0,0
for i in reversed(num_list):
    num += int(i) * int(math.pow(base, cnt))
    cnt += 1

print(num)

