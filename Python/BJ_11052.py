N = int(input())

value = list(map(int,input().split())) # 카드 가격
value.insert(0,0)

lucky = [0] # 최댓값

for i in range(1, N + 1):
    lucky.append(0)
    for j in range(1, i + 1):
        lucky[i] = max(lucky[i], lucky[i - j] + value[j])

print(lucky[N])
