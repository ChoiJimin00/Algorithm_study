from itertools import combinations

N, S = map(int,input().split())
num = list(map(int,input().split()))
cnt = 0

for i in range(1, N+1):
    comb = list(combinations(num,i))

    for index in comb:
        if sum(index) == S:
            cnt += 1

print(cnt)