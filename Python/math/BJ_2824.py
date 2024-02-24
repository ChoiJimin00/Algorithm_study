import math

N = int(input())
A_value = 1
A = list(map(int,input().split()))
for a in A:
    A_value *= a

M = int(input())
B_value = 1
B = list(map(int,input().split()))
for b in B:
    B_value *= b

result = str(math.gcd(A_value, B_value))

if len(result)>=10:
    print(result[-9:])
else:
    print(result)