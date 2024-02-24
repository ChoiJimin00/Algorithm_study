T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    priority = list(map(int,input().split()))

    document = []
    for i in range(N):
        document.append([priority[i], False])
    document[M][1] = True

    cnt = 0
    while True:
        max_prior = max([i[0] for i in document])
        
        prior, state = document.pop(0)
        
        if prior == max_prior:
            cnt+= 1
            
            if state:
                print(cnt)
                break
        else:
            document.append([prior, state])
            