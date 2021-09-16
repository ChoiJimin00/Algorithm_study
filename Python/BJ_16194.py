N = int(input())

money = list(map(int, input().split()))
money.insert(0,0)

result = [0]

for i in range(1, N+1):
  result.append(99999)
  for j in range(1, i+1):
    result[i] = min(result[i], result[i-j]+money[j])

print(result[N])