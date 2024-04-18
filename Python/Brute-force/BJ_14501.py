import sys
input = sys.stdin.readline

def maximum_wage(wage):
    N = len(wage)
    dp = [0]*N
    
    for i in range(N-1, -1, -1):
        if N-i >= wage[i][0]:
            try:
                dp[i] = wage[i][1] + max(dp[i+wage[i][0]:])
            except : 
                dp[i] = wage[i][1]
    return max(dp) 

if __name__ == '__main__':
    N = int(input())
    wage = [list(map(int, input().split())) for _ in range(N)]
    print(maximum_wage(wage))