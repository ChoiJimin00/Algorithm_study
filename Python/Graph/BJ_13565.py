import sys
input = sys.stdin.readline

def dfs():
    global board
    global M,N
    
    stack = []
    for i in range(len(board[0])):
        if board[0][i] == 0:
            stack.append((0,i))
            
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while stack:
        x,y = stack.pop()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            # board 벗어나면 continue
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            
            # 0을 만나면 stack에 넣고, board를 2로 바꿔주기 (1을 만나면 진행 불가능)
            if board[nx][ny] == 0:
                stack.append((nx,ny))
                board[nx][ny] = 2
                
    print('YES' if 2 in board[M-1] else 'NO')
    return

if __name__ == '__main__':
    M,N = map(int,input().split())
    board = [list(map(int, input().rstrip())) for _ in range(M)]

    dfs()