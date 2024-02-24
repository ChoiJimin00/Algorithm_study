import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0]*(N+1)]

for i in range(N):
    dp.append([0]+list(map(int,input().split())))

for i in range(N+1):
    if i == 0:
        continue
    for j in range(N+1):
        if j == 0:
            continue

        if i>1 and j>1: 
            val = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        elif i == 1 and j == 1:
            val = 0
        elif i==1:
            val = dp[i][j-1]
        elif j==1:
            val = dp[i-1][j]
        dp[i][j] += val
        
for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])