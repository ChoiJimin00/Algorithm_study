import sys
input = sys.stdin.readline

def chk(a,b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a-b) == 2:
        return 4
    else:
        return 3
        
def ddr():
    # dp[i][left][right] = Minimum of Sum of power - [ith][left foot][right foot]
    dp = [[[4*len(num) for _ in range(5)] for _ in range(5)] for _ in range(len(num))]
    dp[0][0][0] = 0
    
    for i in range(len(dp)-1):
        a = num[i]
        for left in range(5):
            for right in range(5):
                dp[i+1][left][a] = min(dp[i+1][left][a], dp[i][left][right] + chk(right, a))
                dp[i+1][a][right] = min(dp[i+1][a][right], dp[i][left][right] + chk(left, a))
                
    return min(min(dp[-1]))

if __name__ == '__main__':
    num = list(map(int, input().split()))
    print(ddr())