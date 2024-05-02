import sys
input = sys.stdin.readline

def mul(U, V): # 행렬 U와 V 곱
    n = len(U)
    result = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            result[row][col] = e % 1000

    return result


def square(matrix, B):
    if B == 1:
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                matrix[x][y] %= 1000
        return matrix
    
    tmp = square(matrix, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), matrix)
    else:
        return mul(tmp, tmp)


if __name__ == '__main__':
    N,B = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    result = square(matrix, B)
    for line in result:
        print(*line)