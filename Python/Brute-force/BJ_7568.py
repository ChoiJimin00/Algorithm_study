N = int(input())
body = []

for _ in range(N):
    x,y = map(int, input().split())
    body.append([x,y])
    
for i in body:
    cnt = 1
    for j in body:
        if (i[0]<j[0]) & (i[1]<j[1]):
            cnt += 1
    print(cnt, end=' ')