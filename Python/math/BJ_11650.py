N = int(input())
num = [list(map(int,input().split())) for _ in range(N)]

num.sort(key = lambda x : (x[0], x[1]))

for x in num:
    print(x[0],x[1])
