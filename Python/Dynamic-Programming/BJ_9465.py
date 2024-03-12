import sys
input = sys.stdin.readline

def sticker_val():
    global sticker
    n = len(sticker[0])
    
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
    
    for j in range(2,n):
        for i in range(2):
            dp[i][j] = max(dp[0][j-2], dp[1][j-2], dp[(i+1)%2][j-1]) + sticker[i][j]
                
    return max(dp[0][n-1], dp[1][n-1])

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        sticker = []
        n = int(input())
        
        for _ in range(2):
            sticker.append(list(map(int, input().split())))
            
        print(sticker_val())