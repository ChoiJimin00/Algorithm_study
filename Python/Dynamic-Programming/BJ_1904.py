N = int(input())

tile = [0]*(N+1)

for i in range(1, N+1):
    if i<3:
        tile[i]=i
    else:
        tile[i] = (tile[i-1]+tile[i-2])%15746
    
print(tile[N])