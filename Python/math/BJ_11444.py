# 참고 블로그 : https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11444-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6-%EA%B3%A8%EB%93%9C3-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

MOD = 1000000007

# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열 값

def mul(A,B): # 행렬 A와 행렬 B의 곱
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e%MOD
    return Z
    
def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= MOD
        return A
    
    half = square(A,k//2)
    if k%2 == 0: # 짝수
        return mul(half,half)
    else:
        return mul(mul(half, half),A)
        

if __name__=='__main__':
    N = int(input())
    
    fib_matrix = [[1,1],[1,0]]
    print(square(fib_matrix,N)[0][1])