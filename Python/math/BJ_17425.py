import sys
input = sys.stdin.readline

max = 1000000

dp_sum = [0 for _ in range(max+1)] # 누적합 g(x)를 담는 메모
dp = [0 for _ in range(max+1)] # 해당 값의 약수의 합 f(x)를 담는 메모

for i in range(1,max+1):
    j = 1
    while i * j <= max: # i*j 값이 최대값이 넘지 않을 때까지
        dp[i*j] += i
        j += 1
    dp_sum[i] = dp_sum[i-1] + dp[i]

T = int(input())
    
ans=[]
for _ in range(T):
    N = int(input())
    ans.append(dp_sum[N])
print('\n'.join(map(str, ans))+'\n')