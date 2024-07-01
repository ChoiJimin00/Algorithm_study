import sys
input = sys.stdin.readline

def cal(x,y):
    return (x//3)*3 + (y//3)

def chk_sudoku(n):
    if n == 81:
        for line in sudoku:
            print(''.join(list(map(str, line))))
        return True
    
    x = n//9
    y = n%9
    if sudoku[x][y]:
        return chk_sudoku(n+1)
    else:
        for i in range(1,10):
            if not c1[x][i] and not c2[y][i] and not c3[cal(x,y)][i]:
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = True # 후보
                sudoku[x][y] = i
                
                # 백트래킹
                if chk_sudoku(n+1):
                    return True
                
                # 되돌리기
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = False # 후보 제외
                sudoku[x][y] = 0 
                
    return False
    
    
if __name__ == '__main__':
    sudoku = [list(map(int, input().strip())) for _ in range(9)] 
    
    # 행,열,3*3사각형에 사용된 숫자를 c1, c2, c3에 기록
    # 겹치지 않는 숫자 candidate들을 하나씩 넣어보면서 조건에 위배되는지를 살펴보고 위배된다면 백트래킹으로 다시 값들을 복구하고 다음 후보 숫자를 넣어 탐색
    c1 = [[False]*10 for _ in range(9)] # row
    c2 = [[False]*10 for _ in range(9)] # col
    c3 = [[False]*10 for _ in range(9)] # 3*3 square
    
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]:
                c1[i][sudoku[i][j]] = True   # i행에 A[i][j] 숫자가 사용됨
                c2[j][sudoku[i][j]] = True   # j열에 A[i][j] 숫자가 사용됨
                c3[cal(i,j)][sudoku[i][j]] = True # cal(i,j)번째 square에 A[i][j] 숫자가 사용됨

    chk_sudoku(0)