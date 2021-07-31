# greatest common divisor
a,b = map(int, input().split())

# 나머지가 0일때 까지
while b != 0:
    a,b = b, a % b

print(a)