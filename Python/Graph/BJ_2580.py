import sys
input = sys.stdin.readline


def cal(x,y):
    return (x//3)*3+(y//3)


def dfs(n):
    if n == 81 : 
        for i in range(9):
            print(*sudoku[i])
        return True
    
    x = n//9
    y = n%9
    if sudoku[x][y]:
        return dfs(n+1)
    else:
        for i in range(1,10):
            if not c1[x][i] and not c2[y][i] and not c3[cal(x,y)][i]:
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = True
                sudoku[x][y] = i
                
                if dfs(n+1):
                    return True
                
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = False
                sudoku[x][y] = 0
           

if __name__ == '__main__':
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    c1 = [[False]*10 for _ in range(9)] # row
    c2 = [[False]*10 for _ in range(9)] # col
    c3 = [[False]*10 for _ in range(9)] # rectangle
    
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]:
                c1[i][sudoku[i][j]] = True
                c2[j][sudoku[i][j]] = True
                c3[cal(i,j)][sudoku[i][j]] = True
    dfs(0)