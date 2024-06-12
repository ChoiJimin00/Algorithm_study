import sys
input = sys.stdin.readline

def get_LCS(A,B):
    dp = [[0]*(len(B)) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(1,len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[-1][-1]
                

if __name__ == '__main__':
    N = int(input())
    A = ['0']+input().split()
    B = ['0']+input().split()
    
    print(get_LCS(A,B))