N = int(input())

num = [0]
squares = []
for i in range(1,N+1):
    # 제곱수인 경우 1채워 넣기
    if (i**0.5) % 1 == 0:
        num.append(1)
        squares.append(i)
        continue

    min_val = 1e90
    for sq in squares:
        min_val = min(min_val, num[sq] + num[i-sq])

    num.append(min_val)

print(num[N])