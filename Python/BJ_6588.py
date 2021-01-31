n = 1000000
check = [True] * n

for i in range(2, int(n**0.6)):
    if check[i] == True:
        for j in range (i+i, n, i):
            check[j] = False

while True:
    even = int(input())

    if even == 0:
        break

    for i in range(3, n):
        if check[i]:
            if check[even-i]:
                print(even, '=', i, '+', even - i)
                break
