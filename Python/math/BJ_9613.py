#BJ_9613
import itertools

# 방법 1 ) recursive function
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 방법 2
# def gcd(a_val, b_val):
#     while b_val != 0:
#         a_val = a_val % b_val
#         a_val, b_val = b_val, a_val
#     return a_val

t = int(input())
for i in range(t):
    sum = 0
    num_list = list(map(int, input().split()))
    perm = list(itertools.combinations(num_list[1:], 2))
    for i in perm:
        sum += gcd(i[0],i[1])
    print(sum)




