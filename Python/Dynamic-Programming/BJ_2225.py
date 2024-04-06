import sys
input = sys.stdin.readline

def set_dp():
    max_n = 200
    dp = [[0]*(max_n+1) for _ in range(max_n+1)]
    
    for i in range(max_n+1):
        if i == 0:
            for j in range(max_n+1):
                dp[i][j] = j+1
            continue
        
        for j in range(max_n+1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j]=(dp[i-1][j] + dp[i][j-1])%1000000000
                
    return dp

if __name__ == '__main__':
    N,K = map(int, input().split())
    dp = set_dp()
    print(dp[N-1][K-1])