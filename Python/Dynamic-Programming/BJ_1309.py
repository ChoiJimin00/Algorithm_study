import sys
input = sys.stdin.readline

if __name__ == '__main__':
    dp = [1]*100001
    dp[1] = 3
    for i in range(2,100001):
        dp[i] = (2*dp[i-1] + dp[i-2])%9901
    
    N = int(input())
    print(dp[N])