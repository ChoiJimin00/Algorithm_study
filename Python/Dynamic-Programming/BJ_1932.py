import sys
input = sys.stdin.readline

def dp():
    global triangle
    
    dp = []
    for i in range(len(triangle)):
        dp.append([0]*len(triangle[i]))
    dp[0][0] = triangle[0][0]
                    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
                
            elif j == len(triangle[i]) - 1 :
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                
            else:
                if dp[i-1][j-1] > dp[i-1][j]:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]  
            
    return max(dp[-1])
    

if __name__ == '__main__':
    N = int(input())
    
    triangle = []
    for i in range(N):
        triangle.append(list(map(int,input().split())))
    
    print(dp())
    