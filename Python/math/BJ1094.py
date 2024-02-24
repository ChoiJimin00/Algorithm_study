stick = [64,32,16,8,4,2,1]

X = int(input())

cnt = 0
for s in stick:
    if X >= s:
        X -= s
        cnt += 1

print(cnt)