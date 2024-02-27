import sys
input = sys.stdin.readline

N,K = map(int,input().split())

coins=[]
for _ in range(N):
    coins.append(int(input()))

dp = [0]+[100001] * (K)

for coin in coins:
    for i in range(coin,K+1):
        dp[i] = min(dp[i],dp[i-coin]+1)


print(-1 if dp[K] == 100001 else dp[K])