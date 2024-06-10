import sys
input = sys.stdin.readline

def get_LCS(L1, L2):
    dp = [['']*len(L2) for _ in range(len(L1))]
    
    for i in range(1,len(L1)):
        for j in range(1, len(L2)):
            if L1[i] == L2[j]:
                dp[i][j] = dp[i-1][j-1] + L1[i]
            else:
                if len(dp[i-1][j]) >= len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else: 
                    dp[i][j] = dp[i][j-1]
                
    answer = dp[-1][-1]
    print(len(answer), answer, sep='\n')
    return


if __name__ == '__main__':
    L1 = ' ' + input().strip()
    L2 = ' ' + input().strip()
    
    get_LCS(L1,L2)