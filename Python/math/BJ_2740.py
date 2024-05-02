import sys
input = sys.stdin.readline

def mul(U,V):
    result = [[0]*K for _ in range(N)]
    
    for row in range(N):
        for col in range(K):
            e = 0
            for i in range(M):
                e += U[row][i]*V[i][col]
            result[row][col] = e
            
    for line in result:
        print(*line)
    

if __name__ == '__main__':
    N,M = map(int, input().split())
    m1 = [list(map(int, input().split())) for _ in range(N)]
    
    M,K = map(int, input().split())
    m2 = [list(map(int, input().split())) for _ in range(M)]
    
    mul(m1,m2)