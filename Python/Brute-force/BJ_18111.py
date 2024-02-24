N,M,B = map(int, input().split())
land = []

for _ in range(N):
    land.append(list(map(int,input().split())))
land = sum(land, [])

# 땅 높이의 최댓값, 최솟값 
max_land = max(land)
min_land = min(land)

case = []

for height in range(min_land, max_land+1):    
    if (height*N*M - sum(land)) > B:
        break
    
    time = 0
    for i in range(N*M):
        curr = height-land[i]
        
        if curr < 0 :
            time += 2*abs(curr)
        else:
            time += 1*curr
        
    case.append([time, height])
    
min_time = min(case, key=lambda x : x[0])[0]
max_height = max([i[1] for i in case if i[0] == min_time])

print(min_time, max_height)