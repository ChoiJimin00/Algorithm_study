import sys
input = sys.stdin.readline

def get_LCS(L1,L2):
    dp = [[0]*len(L1) for _ in range(len(L2))]
    
    for i in range(1,len(L2)):
        for j in range(1,len(L1)):
            if L1[j] == L2[i]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
    return dp[-1][-1]
        
if __name__ == '__main__':
    L1 = ' ' + input().strip()
    L2 = ' ' + input().strip()
    
    print(get_LCS(L1,L2))